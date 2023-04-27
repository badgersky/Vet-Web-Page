from django.db import models
from users.models import CustomUser
from pets.models import Pet


class Reservations(models.Model):
    HOUR_CHOICES = [
        (8, '8:00 AM'),
        (9, '9:00 AM'),
        (10, '10:00 AM'),
        (11, '11:00 AM'),
        (12, '12:00 PM'),
        (1, '1:00 PM'),
        (2, '2:00 PM'),
        (3, '3:00 PM'),
        (4, '4:00 PM'),
        (5, '5:00 PM'),
        (6, '6:00 PM'),
    ]

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.IntegerField(choices=HOUR_CHOICES)
