from django.db import models
from datetime import datetime


# Create your models here.

class team(models.Model):
    name = models.CharField(max_length=20)
    number_of_players = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name



class player(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    second_last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=0)
    date_of_birth = models.DateTimeField(default=datetime.now, blank=True),
    height = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    team = models.ForeignKey(team, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    class position(models.TextChoices):
        pivot = 'piv', 'Pivot'
        cierre = 'cie', 'Cierre'
        ala_der = 'a_i', 'Ala_iquierda'
        ala_izq= 'a_d', 'Ala_derecha'
        portero= 'por', 'Portero'
        no_specific= 'nsp','Sin_especificar'


    pos = models.CharField(
        max_length=3,
        choices=position.choices,
        default=position.no_specific,
    )

class competition(models.Model):
    name = models.CharField(max_length=20)
    data = models.DateTimeField(default=datetime.now, blank=True)
    value_rank = models.PositiveIntegerField(default=0)
    teams = models.ManyToManyField(team)

    def __str__(self):
        return self.name





