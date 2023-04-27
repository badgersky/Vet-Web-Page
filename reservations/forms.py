import datetime
from django import forms
from django.core.exceptions import ValidationError
from pets.models import Pet

from . import models


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.Form):
    date = forms.DateField(
        label='Date',
        widget=DateInput,
    )
    hour = forms.ChoiceField(
        label='Hour',
        choices=models.Reservations.HOUR_CHOICES,
    )
    pet = forms.CharField(
        label='Pet Name',
    )

    class Meta:
        model = models.Reservations
        fields = ('date', 'hour')
