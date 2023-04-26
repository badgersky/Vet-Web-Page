from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from . import forms


class LoginView(View):

    def get(self, request):
        form = forms.LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = forms.LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('home:home'))

        return render(request, 'users/login.html', {'form': form})
