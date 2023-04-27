from django import forms
from . import models


class PetForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={
            'name': 'name',
            'placeholder': 'name',
        })
    )
    age = forms.IntegerField(
        label='Age',
        widget=forms.TextInput(attrs={
            'name': 'age',
            'placeholder': 'age',
        })
    )
    species = forms.ChoiceField(
        label='Species',
        choices=models.Pet.SPECIES_CHOICES,
    )
    gender = forms.ChoiceField(
        label='Gender',
        choices=models.Pet.GENDER_CHOICES,
    )

    class Meta:
        model = models.Pet
        fields = '__all__'
        exclude = ['user']


class EditAgeForm(forms.Form):
    age = forms.IntegerField(
        label='Age',
        widget=forms.TextInput(attrs={
            'name': 'age',
            'placeholder': 'age',
        })
    )

    class Meta:
        model = models.Pet
        fields = ('age',)
