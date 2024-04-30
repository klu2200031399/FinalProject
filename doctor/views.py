from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect




def home(request):
    return render(request, 'doctor/base_doctor.html')

def view_appointments(request):
    return render(request, 'doctor/view_appointments.html')



from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Appointment

@login_required
def doctor_dashboard(request):
    if request.user.is_authenticated and hasattr(request.user, 'doctor'):
        doctor = request.user.doctor
        appointments = Appointment.objects.filter(doctor=doctor)
        return render(request, 'doctor_dashboard.html', {'doctor': doctor, 'appointments': appointments})
    else:
        # Handle the case where the user is not authenticated or is not a doctor
        return redirect('login')  # Or any other appropriate action

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment

@login_required
def view_appointments(request):
    doctor = request.user.doctor
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'doctor/view_appointments.html', {'appointments': appointments})

from django.shortcuts import render

def your_view_function(request):
    recent_user = request.user
    return render(request, 'your_template.html', {'user': recent_user})

