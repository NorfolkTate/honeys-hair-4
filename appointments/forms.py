from django import forms
from .models import Appointment

class AppointmentForm(forms.modelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'is_confirmed']