from django.shortcuts import render
from .models import Service, Appointment
from .forms import AppointmentForm
# Create your views here.

def service_list(request):
    services = Service.objects.all()
    return render(request, 'appointments/service_list.html', {'services': services})
