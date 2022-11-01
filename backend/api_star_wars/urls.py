from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('auth/', obtain_auth_token),
    #URLs for planets
    path('planets/', views.PlanetCreateAPIView.as_view(), name="create_planets"),
    path('planets/list/', views.PlanetListAPIView.as_view(), name="list_planets"),
    path('planets/<int:pk>/update', views.PlanetUpdateAPIView.as_view(), name="update_planets"),
    path('planets/<int:pk>/delete', views.PlanetDeleteAPIView.as_view(), name="delete_planets"),
    path('planets/search/', views.PlanetSearchAPIView.as_view(), name='search_planets'),
    path('planets/<int:pk>/', views.PlanetDetailAPIView.as_view(), name="detail_planets"),
    #URLs for directors
    path('directors/', views.DirectorCreateAPIView.as_view(), name="create_director"),
    path('directors/list/', views.DirectorListAPIView.as_view(), name="list_director"),
    path('directors/<int:pk>/update', views.DirectorUpdateAPIView.as_view(), name="update_director"),
    path('directors/<int:pk>/delete', views.DirectorDeleteAPIView.as_view(), name="delete_director"),
    path('directors/search/', views.DirectorSearchAPIView.as_view(), name='search_director'),
    path('directors/<int:pk>/', views.DirectorDetailAPIView.as_view(), name="detail_director"),
    #URLs for productors
    path('productors/', views.ProductorCreateAPIView.as_view(), name="create_productors"),
    path('productors/list/', views.ProductorListAPIView.as_view(), name="list_productors"),
    path('productors/<int:pk>/update', views.ProductorUpdateAPIView.as_view(), name="update_productors"),
    path('productors/<int:pk>/delete', views.ProductorDeleteAPIView.as_view(), name="delete_productors"),
    path('productors/search/', views.ProductorSearchAPIView.as_view(), name='search_productors'),
    path('productors/<int:pk>/', views.ProductorDetailAPIView.as_view(), name="detail_productors"),
    #URLs for movies
    path('movies/', views.MovieCreateAPIView.as_view(), name="create_movies"),
    path('movies/list/', views.MovieListAPIView.as_view(), name="list_movies"),
    path('movies/<int:pk>/update', views.MovieUpdateAPIView.as_view(), name="update_movies"),
    path('movies/<int:pk>/delete', views.MovieDeleteAPIView.as_view(), name="delete_movies"),
    path('movies/search/', views.MovieSearchAPIView.as_view(), name='search_movies'),
    path('movies/<int:pk>/', views.MovieDetailAPIView.as_view(), name="detail_movies"),
    #URLs for characters
    path('characters/', views.CharacterCreateAPIView.as_view(), name="create_characters"),
    path('characters/list/', views.CharacterListAPIView.as_view(), name="list_characters"),
    path('characters/<int:pk>/update', views.CharacterUpdateAPIView.as_view(), name="update_characters"),
    path('characters/<int:pk>/delete', views.CharacterDeleteAPIView.as_view(), name="delete_characters"),
    path('characters/search/', views.CharacterSearchAPIView.as_view(), name='search_characters'),
    path('characters/<int:pk>/', views.CharacterDetailAPIView.as_view(), name="detail_characters")
]
