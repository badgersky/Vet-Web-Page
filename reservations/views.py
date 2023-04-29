import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from . import forms
from . import models
from pets.models import Pet


class ReservationView(View):

    def get(self, request):
        if request.user.is_authenticated:
            form = forms.ReservationForm()
            return render(request, 'reservations/reservations.html', {'form': form})

        messages.add_message(request,
                             messages.WARNING,
                             f'Login first')
        return redirect(reverse('users:login'))

    def post(self, request):
        form = forms.ReservationForm(request.POST)

        if form.is_valid():
            pet = form.cleaned_data.get('pet')
            date = form.cleaned_data.get('date')
            hour = form.cleaned_data.get('hour')

            try:
                Pet.objects.get(name=pet, owner=request.user)
            except Pet.DoesNotExist:
                messages.add_message(request,
                                     messages.WARNING,
                                     f'You don`t have pet with that name.')
                return render(request, 'reservations/reservations.html', {'form': form})
            else:
                if date <= datetime.date.today():
                    messages.add_message(request,
                                         messages.WARNING,
                                         f'You cannot chose date from the past.')
                    return render(request, 'reservations/reservations.html', {'form': form})

                if models.Reservations.objects.filter(date=date, hour=hour).exists():
                    messages.add_message(request,
                                         messages.WARNING,
                                         f'There is reservation for this day and this hour.')
                    return render(request, 'reservations/reservations.html', {'form': form})

                reservation = models.Reservations()
                reservation.owner = request.user
                reservation.pet = Pet.objects.get(name=pet, owner=request.user)
                reservation.date = date
                reservation.hour = hour
                reservation.save()
                return redirect(reverse('home:home'))

        return render(request, 'reservations/reservations.html', {'form': form})


class ShowReservationsView(View):

    def get(self, request):
        reservations = models.Reservations.objects.filter(owner=request.user)
        return render(request, 'reservations/reservations-list.html', {'reservations': reservations})
