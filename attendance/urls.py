from django.urls import path
from .views import employee_day_attendance, employee_history
urlpatterns = [
    path('employees/<str:employee>', employee_history),
    path('employees/<str:employee>/dates/<str:date>', employee_day_attendance),
]