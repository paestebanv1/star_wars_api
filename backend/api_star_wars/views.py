from django.shortcuts import render
from rest_framework import generics, permissions, authentication
from .models import Director, Productor, Planet, Character, Movie
from .serializers import PlanetSerializer, DirectorSerializer, ProductorSerializer, MovieSerializer, CharacterSerializer
from .permissions import IsCustomerPermission


#Views for Characters
class CharacterCreateAPIView(generics.CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class CharacterListAPIView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class CharacterUpdateAPIView(generics.UpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class CharacterDeleteAPIView(generics.DestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class CharacterSearchAPIView(generics.ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        qs = Character.objects.all()
        q = self.request.query_params.get('last_name')
        if q is not None:
            qs = qs.filter(last_name=q)
        return qs

class CharacterDetailAPIView(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]


#Views for Movies
class MovieCreateAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class MovieUpdateAPIView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class MovieDeleteAPIView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class MovieSearchAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        qs = Movie.objects.all()
        q = self.request.query_params.get('title')
        if q is not None:
            qs = qs.filter(title=q)
        return qs

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]


#Views for Planets
class PlanetCreateAPIView(generics.CreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class PlanetDetailAPIView(generics.RetrieveAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class PlanetListAPIView(generics.ListAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class PlanetUpdateAPIView(generics.UpdateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class PlanetDeleteAPIView(generics.DestroyAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]


class PlanetSearchAPIView(generics.ListAPIView):
    serializer_class = PlanetSerializer

    def get_queryset(self):
        qs = Planet.objects.all()
        q = self.request.query_params.get('q')
        if q is not None:
            qs = qs.filter(name=q)
        return qs


#Views for Directors
class DirectorCreateAPIView(generics.CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = ProductorSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class DirectorUpdateAPIView(generics.UpdateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class DirectorDeleteAPIView(generics.DestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class DirectorSearchAPIView(generics.ListAPIView):
    serializer_class = DirectorSerializer

    def get_queryset(self):
        qs = Director.objects.all()
        q = self.request.query_params.get('last_name')
        if q is not None:
            qs = qs.filter(last_name=q)
        return qs

class DirectorDetailAPIView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]


#Views for Productors
class ProductorCreateAPIView(generics.CreateAPIView):
    queryset = Productor.objects.all()
    serializer_class = ProductorSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class ProductorListAPIView(generics.ListAPIView):
    queryset = Productor.objects.all()
    serializer_class = ProductorSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class ProductorUpdateAPIView(generics.UpdateAPIView):
    queryset = Productor.objects.all()
    serializer_class = ProductorSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class ProductorDeleteAPIView(generics.DestroyAPIView):
    queryset = Productor.objects.all()
    serializer_class = ProductorSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]

class ProductorSearchAPIView(generics.ListAPIView):
    serializer_class = ProductorSerializer

    def get_queryset(self):
        qs = Productor.objects.all()
        q = self.request.query_params.get('last_name')
        if q is not None:
            qs = qs.filter(last_name=q)
        return qs

class ProductorDetailAPIView(generics.RetrieveAPIView):
    queryset = Productor.objects.all()
    serializer_class = ProductorSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsCustomerPermission]
