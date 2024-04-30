from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('view_appointment/', views.view_appointments, name='view_appointment'),
    path('your-url/', views.your_view_function, name='your_view'),


    # Add more URLs as needed
]