from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Service, Appointment
from .forms import AppointmentForm
# Create your views here.


@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'appointments/service_list.html', {'services': services})

def book_appointment(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.service = service
            appointment.save()
            return redirect('my_appointments')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointment.html', {'service': service, 'form': form})

