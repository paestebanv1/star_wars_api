from django.db import models
from django.conf import settings
from django.db.models import Q


class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    age = models.IntegerField()

class Productor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

class Planet(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.TextField(max_length=200)
    date_release = models.DateTimeField()
    running_time = models.IntegerField()
    country = models.CharField(max_length=120)
    production_company = models.TextField(max_length=200)
    detail = models.TextField()
    director = models.ForeignKey(Director, default=1, on_delete=models.CASCADE)
    productor = models.ForeignKey(Productor, default=1, on_delete=models.CASCADE)
    planets = models.ManyToManyField(Planet)

class Character(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    place_of_born = models.CharField(max_length=100)
    age = models.IntegerField()
    movies = models.ManyToManyField(Movie)
