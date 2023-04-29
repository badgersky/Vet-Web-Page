from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from . import forms
from . import models
from django.contrib import messages


class AddPetView(View):

    def get(self, request):
        if request.user.is_authenticated:
            form = forms.PetForm()
            return render(request, 'pets/add-pet.html', {'form': form})

        messages.add_message(request,
                             messages.WARNING,
                             f'Login first')
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

        messages.add_message(request,
                             messages.WARNING,
                             f'Login first')
        return redirect(reverse('users:login'))


class DeletePetView(View):

    def get(self, request, pet_id):
        try:
            models.Pet.objects.get(pk=pet_id).delete()
        except models.Pet.DoesNotExist:
            messages.add_message(request,
                                 messages.WARNING,
                                 f'No such pet!'
                                 )

        return redirect(reverse('pets:show'))


class EditAgeView(View):

    def get(self, request, pet_id):
        form = forms.EditAgeForm()
        return render(request, 'partials/edit-age.html', {'form': form, 'pet_id': pet_id})

    def post(self, request, pet_id):
        form = forms.EditAgeForm(request.POST)

        if form.is_valid():
            new_age = form.cleaned_data.get('age')
            pet = models.Pet.objects.get(pk=pet_id)

            if new_age < 0:
                messages.add_message(request,
                                     messages.WARNING,
                                     f'Age cannot be negative!'
                                     )
                return render(request, 'partials/edit-age.html', {'form': form, 'pet_id': pet_id})
            else:
                pet.age = new_age
                pet.save()
                messages.add_message(request,
                                     messages.SUCCESS,
                                     f'Age updated'
                                     )
                return redirect(reverse('pets:show'))

        return render(request, 'partials/edit-age.html', {'form': form, 'pet_id': pet_id})
