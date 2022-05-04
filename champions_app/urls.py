from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Competiciones/', views.Competiciones, name="Competiciones"),
    path('Equipos/', views.Equipos, name='Equipos'),
    path('Estadísticas/', views.Estadísticas, name="Estadísticas"),
    path('Nosotros/', views.Nosotros, name="Nosotros"),
    path('Jugadores/',views.Jugadores, name="Jugadores"),
    path('Historial_de_competición/', views.Historial_de_competición, name="Historial_de_competición")
    ]