from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from . import forms
from . import models


class AddPetView(View):

    def get(self, request):
        if request.user.is_authenticated:
            form = forms.PetForm()
            return render(request, 'pets/add-pet.html', {'form': form})
        return redirect(reverse('users:login'))

    def post(self, request):
        form = forms.PetForm(request.POST)

        if form.is_valid():
            age = form.cleaned_data.get('age')
            name = form.cleaned_data.get('name')
            species = form.cleaned_data.get('species')

            pet = models.Pet()
            pet.age = int(age)
            pet.name = name
            pet.species = species
            pet.owner = request.user
            pet.save()
            return redirect(reverse('home:home'))

        return render(request, 'pets/add-pet.html', {'form': form})


class ShowPetView(View):

    def get(self, request):
        if request.user.is_authenticated:
            pets = models.Pet.objects.filter(owner=request.user)
            return render(request, 'pets/show-pets.html', {'pets': pets})
        return redirect(reverse('users:login'))