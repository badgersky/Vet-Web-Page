from django.shortcuts import render
from django.views import View


class HomeView(View):

    def get(self, reqeust):
        return render(reqeust, 'home/home.html')
