from django.urls import path
from .views import RegisterUserAPIView, LoginUserAPIView, ReminderAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', LoginUserAPIView.as_view(), name='login'),
    path('reminders/', ReminderAPIView.as_view(), name='reminders'),
]
