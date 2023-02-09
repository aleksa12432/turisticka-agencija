from django.shortcuts import render
from .models import Continent, City

def index(request):
    kontinenti = Continent.objects.all()
    gradovi = City.objects.all()
    return render(request, 'home.html', { 'kontinenti': kontinenti, 'gradovi': gradovi })

def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')

def package(request):
    return render(request, 'package.html')

def vacation(request):
    return render(request, 'vacation.html')