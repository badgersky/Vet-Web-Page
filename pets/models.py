from django.core.validators import MinValueValidator
from django.db import models
from users.models import CustomUser


class Pet(models.Model):
    DOG = 'DO'
    CAT = 'CA'
    COW = 'CO'
    PIG = 'PI'
    HORSE = 'HO'
    GUINEA_PIG = 'GP'
    HAMSTER = 'HA'
    RABBIT = 'RA'
    FERRET = 'FE'
    TURTLE = 'TU'
    LIZARD = 'LI'
    SPIDER = 'SP'
    SCORPIO = 'SC'
    SPECIES_CHOICES = [
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (COW, 'Cow'),
        (PIG, 'Pig'),
        (HORSE, 'Horse'),
        (GUINEA_PIG, 'Guinea Pig'),
        (HAMSTER, 'Hamster'),
        (RABBIT, 'Rabbit'),
        (FERRET, 'Ferret'),
        (TURTLE, 'Turtle'),
        (LIZARD, 'Lizard'),
        (SPIDER, 'Spider'),
        (SCORPIO, 'Scorpio'),
    ]

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=2, choices=SPECIES_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(MinValueValidator(0))
