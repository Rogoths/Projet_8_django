from django.shortcuts import render

def home(request):
    return render(request, 'home.html') #requête en premier et chemin vers le template

def result(request):
    return render(request, 'result.html')
