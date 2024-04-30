# admins/views.py
from django.shortcuts import render, redirect
from .models import Doctor, Feedback
from .forms import DoctorForm


def admin_home(request):
    return render(request, 'admins/home.html')


from django.core.mail import send_mail
from django.conf import settings

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            new_doctor = form.save()
            # Send email after saving the doctor
            subject = 'Your Doctor Account Details'
            message = f'Username: {new_doctor.name}\nPassword: {new_doctor.password}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [new_doctor.email]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('admins:home')
    else:
        form = DoctorForm()

    return render(request, 'admins/add_doctor.html', {'form': form})

def view_feedbacks(request):
    feedbacks = Feedback.objects.all()
    context = {'feedbacks': feedbacks}
    return render(request, 'admins/view_feedbacks.html', context)

# admins/views.py
from django.shortcuts import render
from Module.models import Appointment

def view_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'admins/view_appointments.html', {'appointments': appointments})

