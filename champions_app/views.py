from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def competitions(request):
    return render(request, 'competitions.html')

def teams(request):
    return render(request, 'teams.html')

def statistics(request):
    return render(request, 'statistics.html')

def us(request):
    return render(request, 'us.html')


def competition_history(request):
    return render(request, 'competition_history.html')

