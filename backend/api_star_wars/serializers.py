from rest_framework import serializers
from .models import Director, Productor, Planet, Character, Movie


class PlanetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planet
        fields=[
            'id',
            'name'
        ]


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields=[
            'id',
            'first_name',
            'last_name',
            'genre',
            'age'
        ]


class ProductorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Productor
        fields=[
            'id',
            'first_name',
            'last_name',
            'age'
        ]


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields=[
            'id',
            'title',
            'date_release',
            'running_time',
            'country',
            'production_company',
            'detail',
            'director',
            'productor',
            'planets'
        ]


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields=[
            'id',
            'first_name',
            'last_name',
            'place_of_born',
            'age',
            'movies'
        ]
