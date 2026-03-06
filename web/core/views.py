import json
import requests
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, View
from django.contrib.auth.views import LoginView, LogoutView

from .models import Day, Exercise, Submission, UserProgress


class HomeView(TemplateView):
    """Dashboard showing all days and user progress."""
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        days = Day.objects.prefetch_related('exercises').all()
        day_data = []
        for day in days:
            total = day.exercises.count()
            passed = 0
            is_validated = False
            percentage = 0
            if self.request.user.is_authenticated:
                progress = UserProgress.objects.filter(user=self.request.user, day=day).first()
                if progress:
                    passed = progress.exercises_passed
                    is_validated = progress.is_validated
                    percentage = progress.percentage
            day_data.append({
                'day': day,
                'total': total,
                'passed': passed,
                'is_validated': is_validated,
                'percentage': percentage,
            })
        context['day_data'] = day_data
        return context


class DayDetailView(DetailView):
    """List all exercises for a given day with status."""
    model = Day
    template_name = 'day_detail.html'
    context_object_name = 'day'
    slug_field = 'number'
    slug_url_kwarg = 'day_number'

    def dispatch(self, request, *args, **kwargs):
        day_number = self.kwargs.get('day_number')
        if int(day_number) != 1 and not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        day = self.object
        exercises = day.exercises.all().with_difficulty_order()

        exercise_data = []
        for ex in exercises:
            status = None
            if self.request.user.is_authenticated:
                last_sub = Submission.objects.filter(
                    user=self.request.user, exercise=ex, status='pass'
                ).first()
                if last_sub:
                    status = 'pass'
                else:
                    last_sub = Submission.objects.filter(
                        user=self.request.user, exercise=ex
                    ).first()
                    if last_sub:
                        status = last_sub.status
            exercise_data.append({
                'exercise': ex,
                'status': status,
            })

        progress = None
        if self.request.user.is_authenticated:
            progress = UserProgress.objects.filter(user=self.request.user, day=day).first()

        context['exercise_data'] = exercise_data
        context['progress'] = progress
        return context


class ExerciseDetailView(DetailView):
    """Show exercise description and code submission form."""
    model = Exercise
    template_name = 'exercise_detail.html'
    context_object_name = 'exercise'

    def get_object(self, queryset=None):
        day = get_object_or_404(Day, number=self.kwargs.get('day_number'))
        return get_object_or_404(Exercise, day=day, number=self.kwargs.get('exercise_number'))

    def dispatch(self, request, *args, **kwargs):
        day_number = self.kwargs.get('day_number')
        if int(day_number) != 1 and not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercise = self.object

        last_submission = None
        if self.request.user.is_authenticated:
            last_submission = Submission.objects.filter(
                user=self.request.user, exercise=exercise
            ).first()

        context['day'] = exercise.day
        context['last_submission'] = last_submission
        return context


class SubmitCodeView(View):
    """Handle code submission via AJAX."""
    def post(self, request, day_number, exercise_number):
        if int(day_number) != 1 and not request.user.is_authenticated:
            return JsonResponse({'error': 'Unauthorized'}, status=401)
            
        day = get_object_or_404(Day, number=day_number)
        exercise = get_object_or_404(Exercise, day=day, number=exercise_number)

        try:
            body = json.loads(request.body)
            code = body.get('code', '').strip()
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        if not code:
            return JsonResponse({'error': 'No code submitted'}, status=400)
            
        if len(code) > 50000:
            return JsonResponse({'error': 'Payload too large. Limit is 50000 characters.'}, status=400)

        # Send to runner
        try:
            runner_url = f"{settings.RUNNER_URL}/run"
            payload = {
                'code': code,
                'day_number': day.number,
                'exercise_id': exercise.exercise_id,
                'language': day.language,
                'timeout': exercise.timeout_seconds if exercise.has_timeout else None,
            }
            resp = requests.post(runner_url, json=payload, timeout=60)
            result = resp.json()
        except requests.exceptions.RequestException as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Runner unavailable: {str(e)}'
            }, status=503)

        # Save submission if authenticated
        status = result.get('status', 'error')
        error_message = result.get('message', '')

        if request.user.is_authenticated:
            Submission.objects.create(
                user=request.user,
                exercise=exercise,
                code=code,
                status=status,
                error_message=error_message,
            )

            # Update progress
            _update_progress(request.user, day)

        return JsonResponse({
            'status': status,
            'message': error_message,
        })


def _update_progress(user, day):
    """Recalculate user's progress for a day."""
    exercises = day.exercises.all()
    total = exercises.count()
    passed = 0
    for ex in exercises:
        if Submission.objects.filter(user=user, exercise=ex, status='pass').exists():
            passed += 1

    progress, _ = UserProgress.objects.get_or_create(
        user=user, day=day,
        defaults={'total_exercises': total}
    )
    progress.exercises_passed = passed
    progress.total_exercises = total

    # Validate day
    if total > 0:
        pct = (passed / total) * 100
        if day.is_critical:
            progress.is_validated = (passed == total)
        else:
            progress.is_validated = (pct >= day.passing_threshold)

    progress.save()


class UserRegisterView(CreateView):
    """User registration."""
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class UserLoginView(LoginView):
    """User login."""
    template_name = 'login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    """User logout."""
    next_page = 'home'
