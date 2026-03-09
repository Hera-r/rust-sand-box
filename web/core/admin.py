from django.contrib import admin
from .models import Day, Exercise, Submission, UserProgress

class ExerciseInline(admin.TabularInline):
    model = Exercise
    extra = 0
    show_change_link = True
    fields = ('number', 'title', 'difficulty', 'has_timeout')

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'is_critical', 'passing_threshold', 'language')
    list_editable = ('is_critical', 'passing_threshold', 'language')
    search_fields = ('title', 'description')
    ordering = ('number',)
    inlines = [ExerciseInline]
    fieldsets = (
        ('General Info', {
            'fields': ('number', 'title', 'description')
        }),
        ('Settings', {
            'fields': ('language', 'is_critical', 'passing_threshold')
        }),
    )

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('day', 'number', 'title', 'difficulty', 'has_timeout', 'timeout_seconds')
    list_filter = ('day', 'difficulty', 'has_timeout')
    list_editable = ('difficulty', 'has_timeout', 'timeout_seconds')
    search_fields = ('title', 'description', 'examples', 'tutorial')
    ordering = ('day', 'number')
    autocomplete_fields = ('day',)
    fieldsets = (
        ('Core', {
            'fields': ('day', 'number', 'title', 'difficulty')
        }),
        ('Content', {
            'fields': ('description', 'tutorial', 'examples', 'performance_notes')
        }),
        ('Code execution', {
            'fields': ('starter_code', 'function_signature', 'has_timeout', 'timeout_seconds')
        })
    )

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'exercise', 'status', 'submitted_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('user__username', 'exercise__title', 'code')
    autocomplete_fields = ('user', 'exercise')
    readonly_fields = ('submitted_at',)
    date_hierarchy = 'submitted_at'
    ordering = ('-submitted_at',)

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'exercises_passed', 'total_exercises', 'percentage', 'is_validated')
    list_filter = ('is_validated', 'day')
    search_fields = ('user__username', 'day__title')
    autocomplete_fields = ('user', 'day')
    ordering = ('-is_validated', 'user')
    readonly_fields = ('percentage',)
