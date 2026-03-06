from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('day/<int:day_number>/', views.DayDetailView.as_view(), name='day_detail'),
    path('day/<int:day_number>/ex/<int:exercise_number>/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
    path('day/<int:day_number>/ex/<int:exercise_number>/submit/', views.SubmitCodeView.as_view(), name='submit_code'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
