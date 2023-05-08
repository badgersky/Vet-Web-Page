import datetime
from django import forms
from django.core.exceptions import ValidationError
from pets.models import Pet

from . import models


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        user = kwargs.get('user')

        names = [(pet.name, pet.name) for pet in Pet.objects.filter(owner=user)]
        self.fields.get('pet').choices = names

    date = forms.DateField(
        label='Date',
        widget=DateInput,
    )
    hour = forms.ChoiceField(
        label='Hour',
        choices=models.Reservations.HOUR_CHOICES,
    )
    pet = forms.ChoiceField(
        label='Pet Name',
    )

    class Meta:
        model = models.Reservations
        fields = ('date', 'hour')
