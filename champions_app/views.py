from django.shortcuts import render

# Create your views here.
from champions_app.models import team,competition,player


def home(request):
    return render(request, 'home.html')

def Competiciones(request):
    competitionsViews= competition.objects.all()
    return render(request, 'Competiciones.html',{"competitionsViews":competitionsViews})

def Equipos(request):
    teamViews= team.objects.all()
    return render(request, 'Equipos.html', {"teamViews": teamViews})

def Jugadores(request):
    jugadoresViews= player.objects.all()
    teamPlayerViews = team.objects.all()
    return render(request,'Jugadores.html',{"jugadoresViews":jugadoresViews, "teamViews": teamPlayerViews})

def Estadísticas(request):
    return render(request, 'Estadísticas.html')

def Nosotros(request):
    return render(request, 'Nosotros.html')


def Historial_de_competición(request):
    return render(request, 'Historial_de_competición.html', {'nbar': 'Equipos'})



