from django.urls import path

from . import views

app_name = 'pets'

urlpatterns = [
    path('add/', views.AddPetView.as_view(), name='add'),
    path('show/', views.ShowPetView.as_view(), name='show'),
    path('delete/<pet_id>/', views.DeletePetView.as_view(), name='delete'),
    path('edit/<pet_id>/', views.EditAgeView.as_view(), name='edit'),
]
