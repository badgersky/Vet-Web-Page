from django.urls import path

from . import views

app_name = 'reservations'

urlpatterns = [
    path('reserve/', views.ReservationView.as_view(), name='reserve'),
    path('list/', views.ShowReservationsView.as_view(), name='reservation-list'),
]
