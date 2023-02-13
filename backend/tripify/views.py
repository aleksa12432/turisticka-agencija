from django.shortcuts import render
from .models import Continent, Country, City, Aranzman, Termin, Smestaj, Smestaj_slika, Tip_prevoza
from datetime import datetime
from django.http import (HttpResponseBadRequest)
from django.core.paginator import Paginator
import time
from django.db.models import Sum, Q, F, OuterRef, Min, Subquery

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

    kontinenti = Continent.objects.all()
    transporti = Tip_prevoza.objects.all()

    aranzmani = Aranzman.objects.all()

    start_time = time.time()

    page = 1
    num_per_page = 50

    if "name" in request.GET and request.GET["name"] != "":
        aranzmani = aranzmani.filter(naziv__icontains=request.GET["name"])
    
    # if "continent" in request.GET and request.GET["continent"] != "":
    
    if "transport" in request.GET and request.GET["transport"] != "":
        aranzmani = aranzmani.filter(prevoz__id=request.GET["transport"])

    if "arrival" in request.GET and request.GET["arrival"] != "":
        aranzmani = aranzmani.filter(
            polazak__date=datetime.strptime(request.GET["arrival"], '%Y-%m-%d')
        )

    if "arrival" in request.GET and request.GET["arrival"] != "":
        datum_polaska = datetime.strptime(request.GET["arrival"], '%Y-%m-%d')
        aranzmani = aranzmani.filter(
            polazak__date=datum_polaska
        )
    
        if "leaving" in request.GET and request.GET["leaving"] != "":
            datum_odlaska = datetime.strptime(request.GET["leaving"], '%Y-%m-%d')
            broj_dana = (datum_odlaska - datum_polaska).days
            print(f"Broj dana: {broj_dana}")
            aranzmani = aranzmani.filter(
                duzina=broj_dana
            )
    

    aranzmani = aranzmani.annotate(cena_prevoza=Sum('termin__smestaj__cena_prevoza'))

    # aranzmani = aranzmani.annotate(ime_grada=F('termin__smestaj__grad__name'))
    
    first_term = Termin.objects.filter(aranzman=OuterRef('pk')).order_by('vreme_stizanja').values('smestaj__grad__name', 'smestaj__grad__image', 'smestaj__grad__country__continent__id')[:1]


    aranzmani = aranzmani.annotate(
        ime_grada=Subquery(first_term.values('smestaj__grad__name'))
    )

    aranzmani = aranzmani.annotate(
        slika_grada=Subquery(first_term.values('smestaj__grad__image'))
    )

    aranzmani = aranzmani.annotate(
        continent_id=Subquery(first_term.values('smestaj__grad__country__continent__id'))
    )

    if "continent" in request.GET and request.GET["continent"] != "":
        aranzmani = aranzmani.filter(continent_id=int(request.GET["continent"]))

    novi_aranzmani = list(
        aranzmani.filter(polazak__gt=datetime.now()).order_by('polazak')
    )

    novi_aranzmani.extend(
        list(
            aranzmani.filter(polazak__lt=datetime.now()).order_by('-polazak')
        )
    )

    print(len(novi_aranzmani))

    print(f"Pretraga izvrsena za: {time.time() - start_time}s")


    if "page" in request.GET:
        page = int(request.GET["page"])

    if "show" in request.GET:
        num_per_page = int(request.GET["show"])

    p = Paginator(novi_aranzmani, num_per_page)

    return render(request, 'package.html', { 'kontinenti': kontinenti, 'transporti': transporti, 'aranzmani': p.page(page) })

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
    smestaji = []

    for termin in termini:
        cena += termin.smestaj.cena_prevoza
        smestaji.append(termin.smestaj)

    
    slike_smestaja = Smestaj_slika.objects.filter(smestaj__in=smestaji)

    return render(request, 'vacation.html', { 'aranzman': aranzman, 'termini': termini, 'cena': cena, 'slike_smestaja': slike_smestaja })

def cities(request):

    id = None
    gradovi = None
    
    try:
        id = request.GET["id"]
        kontinent = Continent.objects.get(pk=id)
        drzave = list(Country.objects.filter(continent=kontinent))
        gradovi = City.objects.filter(country__in=drzave)
    except:
        return HttpResponseBadRequest("ID missing/unknown")
    
    return render(request, 'cities.html', { 'gradovi': gradovi })

def city(request):

    id = None
    grad = None
    page = 1

    aranzmani = []
    aranzmani_list = []

    try:
        id = request.GET["id"]
        
        if "page" in request.GET:
            page = request.GET["page"]

        grad = City.objects.get(pk=id)
        smestaji = list(Smestaj.objects.filter(grad=grad))
        termini = list(Termin.objects.filter(smestaj__in=smestaji, vreme_stizanja__gt=datetime.today()).order_by('vreme_stizanja'))
        termini.extend(list(Termin.objects.filter(smestaj__in=smestaji, vreme_stizanja__lt=datetime.today()).order_by('-vreme_stizanja')))
        for termin in termini:
            if not termin.aranzman in aranzmani:
                aranzmani.append(termin.aranzman)
    except:
        return HttpResponseBadRequest("ID missing/unknown")

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

    p = Paginator(aranzmani_list, 50)

    return render(request, 'city.html', { 'grad': grad, 'aranzmani': p.page(page), 'id': id })
