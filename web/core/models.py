from django.db import models
from django.contrib.auth.models import User


class Day(models.Model):
    """A training day containing multiple exercises."""
    number = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_critical = models.BooleanField(
        default=False,
        help_text="If True, 100% of exercises must pass to validate this day."
    )
    language = models.CharField(max_length=20, default='rust')
    passing_threshold = models.PositiveIntegerField(
        default=80,
        help_text="Minimum percentage of exercises to pass (ignored if is_critical)."
    )

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"Day {self.number}: {self.title}"

class ExerciseQuerySet(models.QuerySet):
    def with_difficulty_order(self):
        from django.db.models import Case, When, Value, IntegerField
        return self.annotate(
            difficulty_order=Case(
                When(difficulty='easy', then=Value(1)),
                When(difficulty='medium', then=Value(2)),
                When(difficulty='hard', then=Value(3)),
                default=Value(4),
                output_field=IntegerField(),
            )
        ).order_by('difficulty_order', 'number')

class Exercise(models.Model):
    """An individual exercise within a Day."""
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='exercises')
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    examples = models.TextField(
        blank=True,
        help_text="Input/output examples for this exercise."
    )
    tutorial = models.TextField(
        blank=True,
        help_text="French tutorial for this exercise."
    )
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    has_timeout = models.BooleanField(default=False)
    timeout_seconds = models.PositiveIntegerField(default=10)
    performance_notes = models.TextField(
        blank=True,
        help_text="Pedagogical notes about algorithmic complexity."
    )
    starter_code = models.TextField(
        blank=True,
        help_text="Template code shown to the user."
    )
    function_signature = models.CharField(
        max_length=500,
        blank=True,
        help_text="Expected function signature."
    )

    objects = ExerciseQuerySet.as_manager()

    class Meta:
        ordering = ['day', 'number']
        unique_together = ['day', 'number']

    def __str__(self):
        return f"Day {self.day.number} - Ex{self.number:02d}: {self.title}"

    @property
    def exercise_id(self):
        return f"ex{self.number:02d}"


class Submission(models.Model):
    """A code submission by a user for an exercise."""
    STATUS_CHOICES = [
        ('pass', 'Pass'),
        ('fail', 'Fail'),
        ('error', 'Compilation Error'),
        ('timeout', 'Timeout'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='submissions')
    code = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    error_message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.user.username} - {self.exercise} - {self.status}"


class UserProgress(models.Model):
    """Tracks a user's progress on a particular Day."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='user_progress')
    exercises_passed = models.PositiveIntegerField(default=0)
    total_exercises = models.PositiveIntegerField(default=0)
    is_validated = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'day']

    def __str__(self):
        return f"{self.user.username} - Day {self.day.number}: {self.exercises_passed}/{self.total_exercises}"

    @property
    def percentage(self):
        if self.total_exercises == 0:
            return 0
        return round((self.exercises_passed / self.total_exercises) * 100)
