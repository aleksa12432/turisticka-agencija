from django.shortcuts import render
from .models import Continent, City, Aranzman, Termin, Smestaj_slika
from datetime import datetime
from django.http import (HttpResponseBadRequest)

def index(request):

    kontinenti = Continent.objects.all()
    gradovi = City.objects.all()

    aranzmani = Aranzman.objects.filter(polazak__gt=datetime.today()).order_by('polazak')[:3]

    aranzmani_list = []

    for aranzman in aranzmani:

        l = []

        l.append(aranzman)

        termin = Termin.objects.filter(
            aranzman=aranzman
        ).order_by('vreme_stizanja')[0]
        
        cena = aranzman.cena

        termini = Termin.objects.filter(aranzman=aranzman)

        for t in termini:
            cena += t.smestaj.cena_prevoza

        l.append(termin)
        l.append(cena)

        aranzmani_list.append(l)

    print(aranzmani_list)

    return render(request, 'home.html', { 'kontinenti': kontinenti, 'gradovi': gradovi, 'aranzmani': aranzmani_list })

def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')

def package(request):
    return render(request, 'package.html')

def vacation(request):

    id = None
    aranzman = None

    try:
        id = request.GET["id"]
        aranzman = Aranzman.objects.get(pk=id)
    except:
        return HttpResponseBadRequest("ID missing/unknown")
    
    termini = Termin.objects.filter(aranzman=aranzman)

    cena = aranzman.cena

    for termin in termini:
        cena += termin.smestaj.cena_prevoza

    return render(request, 'vacation.html', { 'aranzman': aranzman, 'termini': termini, 'cena': cena })