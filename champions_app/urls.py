from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('competitions/', views.competitions, name="competitions"),
    path('teams/', views.teams, name='teams'),
    path('statistics/', views.statistics, name="statistics"),
    path('us/', views.us, name="us"),
    path('competition_history/', views.competition_history, name="competition_history")
    ]