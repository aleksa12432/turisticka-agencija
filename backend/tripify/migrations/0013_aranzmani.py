from django.db import migrations
from datetime import datetime
import dateutil.relativedelta
import random
import calendar
import time

BROJ_PROSLIH_ARANZMANA = 10000
BROJ_AKTUELNIH_ARANZMANA = 50000
MAX_LOKACIJA_PO_ARANZMANU = 3

def get_random_day(month, year):
    while True:
        try:
            day = random.randint(1, 31)
            date = datetime(year, month, day).day
            break
        except ValueError: # ako dan ne postoji (npr 30 februar)
            continue
    return date


def add_aranzmane(apps, schema_editor):

    City = apps.get_model('tripify', 'City')
    Aranzman = apps.get_model('tripify', 'Aranzman')
    Termin = apps.get_model('tripify', 'Termin')
    Smestaj = apps.get_model('tripify', 'Smestaj')
    Tip_prevoza = apps.get_model('tripify', 'Tip_prevoza')
    Tipovi_smestaja = apps.get_model('tripify', 'Tipovi_smestaja')

    tipovi_prevoza = Tip_prevoza.objects.all()
    tipovi_smestaja = Tipovi_smestaja.objects.all()

    prosli = BROJ_PROSLIH_ARANZMANA

    datum_vreme = datetime.today()

    # krecemo od pre 2 meseca da pravimo prosle (zastarele) termine
    vreme = datum_vreme + dateutil.relativedelta.relativedelta(months=-2)

    aranzman_instances = []
    termin_instances = []

    print("Generisem zastarele termine...")

    start_time = time.time()

    # zauzeti_gradovi = {
    #       2022: { # 2022 godina
    #           1: [ # januar
    #               Beograd
    #           ],
    #           2: [
    #               Kragujevac
    #           ],
    #       },
    # }
    # if city in zauzeti_gradovi[2022][1]
    zauzeti_gradovi = {
        
    }

    while prosli > 0:

        mesec = vreme.month
        godina = vreme.year
        dan = get_random_day(mesec, godina) # izaberi random dan
        prevoz = random.choice(tipovi_prevoza)
        tip_smestaja = random.choice(tipovi_smestaja)

        # print(f"Termin pocinje: {dan}. {mesec}. {godina}")

        if godina not in zauzeti_gradovi:
            zauzeti_gradovi[godina] = {}
        
        if mesec not in zauzeti_gradovi[godina]:
            zauzeti_gradovi[godina][mesec] = []

        cities = City.objects.exclude(name__in=zauzeti_gradovi[godina][mesec])

        if len(cities) < MAX_LOKACIJA_PO_ARANZMANU:
            vreme += dateutil.relativedelta.relativedelta(months=-1)
            # print("Pomeram mesec unazad!")
            continue

        # biramo nasumicni grad
        city = random.choice(cities)

        zauzeti_gradovi[godina][mesec].append(city.name)

        # print(f"Izabran grad: {city.name}")

        smestaj = random.choice(Smestaj.objects.filter(grad=city))
        # print(f"Izabran smestaj u gradu: {smestaj.name}")

        gradovi = [ city ]
        smestaji = [ smestaj ]

        duzine_termina = [ ]

        datetime_stizanja = [ ]

        duzina_trajanja = random.randint(7, 14)

        broj_lokacija = random.randint(1, MAX_LOKACIJA_PO_ARANZMANU)

        # print(f"Aranzman obuhvata {broj_lokacija} grad(a), ukupno trajanje {duzina_trajanja}")

        for i in range(broj_lokacija):

            random_sat = random.randint(0, 23)
            random_minut = random.randint(0, 59)

            ostalo_dana = duzina_trajanja - sum(duzine_termina)

            dt = datetime(godina, mesec, dan, random_sat, random_minut) + dateutil.relativedelta.relativedelta(days=sum(duzine_termina))
            
            datetime_stizanja.append(dt)

            if godina not in zauzeti_gradovi:
                zauzeti_gradovi[godina] = {}

            if mesec not in zauzeti_gradovi[godina]:
                zauzeti_gradovi[godina][mesec] = []

            if i != 0:

                c = City.objects.exclude(name__in=zauzeti_gradovi[godina][mesec])

                izabrani_grad = random.choice(c)

                zauzeti_gradovi[godina][mesec].append(izabrani_grad.name)

                smestaj = random.choice(Smestaj.objects.filter(grad=izabrani_grad))

                # print(f"Termin {i+1}, izabran grad: {izabrani_grad.name}, izabran smestaj: {smestaj.name}")

                gradovi.append(izabrani_grad)
                smestaji.append(smestaj)


            if i == broj_lokacija - 1:
                duzine_termina.append(ostalo_dana)
                break

            duzine_termina.append(random.randint(1, ostalo_dana - (broj_lokacija - i)))

        # for dt, duzina, grad, smestaj in zip(datetime_stizanja, duzine_termina, gradovi, smestaji):
        #     print(f"Termin: {dt.strftime('%d. %m. %Y., %H:%M')},\n\ttrajanje: {duzina} dana\n\tgrad:{grad.name}\n\tsmestaj:{smestaj.name}")

        
        polazak_vreme = datetime_stizanja[0] - dateutil.relativedelta.relativedelta(hours=random.randint(1,5), minutes=random.randint(0,59))

        rec = ''

        if datetime_stizanja[0].hour < 12:
            rec = "morning"
        elif datetime_stizanja[0].hour < 19:
            rec = "afternoon"
        else:
            rec = "evening"

        opis = f"Departure from {'airport' if prevoz.name == 'airplane' else 'platform'} at {polazak_vreme.strftime('%d. %m %Y., %H:%M')}\nLorem ipsum\nArrival in {city.name} in the {rec} hours"

        trenutni_aranzman = Aranzman(
            naziv=f"{city.name} {calendar.month_name[mesec]} {godina}",
            opis=opis,
            prevoz=prevoz,
            smestaj=tip_smestaja,
            cena=random.randint(500,3000),
            polazak=polazak_vreme,
            duzina=duzina_trajanja
        )

        aranzman_instances.append(trenutni_aranzman)

        for s, dt in zip(smestaji, datetime_stizanja):
            termin_instances.append(Termin(
                aranzman=trenutni_aranzman,
                smestaj=s,
                vreme_stizanja=dt
            ))

        prosli -= 1

    print("Generisem nove aranzmane...")

    novi = BROJ_AKTUELNIH_ARANZMANA

    # krecemo mesec unapred za nove aranzmane 
    vreme = datum_vreme + dateutil.relativedelta.relativedelta(months=1)

    while novi > 0:

        mesec = vreme.month
        godina = vreme.year
        dan = get_random_day(mesec, godina) # izaberi random dan
        prevoz = random.choice(tipovi_prevoza)
        tip_smestaja = random.choice(tipovi_smestaja)

        # print(f"Termin pocinje: {dan}. {mesec}. {godina}")

        if godina not in zauzeti_gradovi:
            zauzeti_gradovi[godina] = {}
        
        if mesec not in zauzeti_gradovi[godina]:
            zauzeti_gradovi[godina][mesec] = []

        cities = City.objects.exclude(name__in=zauzeti_gradovi[godina][mesec])

        if len(cities) < MAX_LOKACIJA_PO_ARANZMANU:
            vreme += dateutil.relativedelta.relativedelta(months=1)
            # print("Pomeram mesec unapred!")
            continue

        # biramo nasumicni grad
        city = random.choice(cities)

        zauzeti_gradovi[godina][mesec].append(city.name)

        # print(f"Izabran grad: {city.name}")

        smestaj = random.choice(Smestaj.objects.filter(grad=city))
        # print(f"Izabran smestaj u gradu: {smestaj.name}")

        gradovi = [ city ]
        smestaji = [ smestaj ]

        duzine_termina = [ ]

        datetime_stizanja = [ ]

        duzina_trajanja = random.randint(7, 14)

        broj_lokacija = random.randint(1, MAX_LOKACIJA_PO_ARANZMANU)

        # print(f"Aranzman obuhvata {broj_lokacija} grad(a), ukupno trajanje {duzina_trajanja}")

        for i in range(broj_lokacija):

            random_sat = random.randint(0, 23)
            random_minut = random.randint(0, 59)

            ostalo_dana = duzina_trajanja - sum(duzine_termina)

            dt = datetime(godina, mesec, dan, random_sat, random_minut) + dateutil.relativedelta.relativedelta(days=sum(duzine_termina))
            
            datetime_stizanja.append(dt)

            if godina not in zauzeti_gradovi:
                zauzeti_gradovi[godina] = {}

            if mesec not in zauzeti_gradovi[godina]:
                zauzeti_gradovi[godina][mesec] = []

            if i != 0:

                c = City.objects.exclude(name__in=zauzeti_gradovi[godina][mesec])

                izabrani_grad = random.choice(c)

                zauzeti_gradovi[godina][mesec].append(izabrani_grad.name)

                smestaj = random.choice(Smestaj.objects.filter(grad=izabrani_grad))

                # print(f"Termin {i+1}, izabran grad: {izabrani_grad.name}, izabran smestaj: {smestaj.name}")

                gradovi.append(izabrani_grad)
                smestaji.append(smestaj)


            if i == broj_lokacija - 1:
                duzine_termina.append(ostalo_dana)
                break

            duzine_termina.append(random.randint(1, ostalo_dana - (broj_lokacija - i)))

        # for dt, duzina, grad, smestaj in zip(datetime_stizanja, duzine_termina, gradovi, smestaji):
        #     print(f"Termin: {dt.strftime('%d. %m. %Y., %H:%M')},\n\ttrajanje: {duzina} dana\n\tgrad:{grad.name}\n\tsmestaj:{smestaj.name}")

        
        polazak_vreme = datetime_stizanja[0] - dateutil.relativedelta.relativedelta(hours=random.randint(1,5), minutes=random.randint(0,59))

        rec = ''

        if datetime_stizanja[0].hour < 12:
            rec = "morning"
        elif datetime_stizanja[0].hour < 19:
            rec = "afternoon"
        else:
            rec = "evening"

        opis = f"Departure from {'airport' if prevoz.name == 'airplane' else 'platform'} at {polazak_vreme.strftime('%d. %m %Y., %H:%M')}\nLorem ipsum\nArrival in {city.name} in the {rec} hours"

        trenutni_aranzman = Aranzman(
            naziv=f"{city.name} {calendar.month_name[mesec]} {godina}",
            opis=opis,
            prevoz=prevoz,
            smestaj=tip_smestaja,
            cena=random.randint(500,3000),
            polazak=polazak_vreme,
            duzina=duzina_trajanja
        )

        aranzman_instances.append(trenutni_aranzman)

        for s, dt in zip(smestaji, datetime_stizanja):
            termin_instances.append(Termin(
                aranzman=trenutni_aranzman,
                smestaj=s,
                vreme_stizanja=dt
            ))

        novi -= 1
    
    print(f"{len(aranzman_instances)} aranzmana generisano za {time.time() - start_time} sekundi! Popunjavam!")

    print("Popunjavam aranzmane...")

    for aranzman in aranzman_instances:
        aranzman.save()

    # Aranzman.objects.bulk_create(aranzman_instances, batch_size=100)

    if (len(aranzman_instances) != BROJ_PROSLIH_ARANZMANA + BROJ_AKTUELNIH_ARANZMANA):
        raise AssertionError("Losa generacija termina! Zaustavljam!")
    
    print("Popunjavam termine...")

    for termin in termin_instances:
        termin.save()

    # Termin.objects.bulk_create(termin_instances, batch_size=100)

class Migration(migrations.Migration):

    dependencies = [
        ("tripify", "0012_alter_aranzman_naziv"),
    ]

    operations = [
        migrations.RunPython(add_aranzmane)
    ]
