from django.db import migrations
import itertools
import random

BROJ_SMESTAJA_PO_GRADU = 3

def napravi_smestaje(apps, schema_editor):
    
    Smestaj = apps.get_model('tripify', 'Smestaj')
    City = apps.get_model('tripify', 'City')
    tipovi_smestaja = apps.get_model('tripify', 'Tipovi_smestaja').objects.all()
    tipovi_soba = apps.get_model('tripify', 'Tip_sobe').objects.all()

    smestaj_instances = []

    print("Popunjavam niz smestaja...")

    for city, i in itertools.product(
        City.objects.all(), 
        range(BROJ_SMESTAJA_PO_GRADU)):

        random_name = ''
        with open("resources/smestaj_tekst.txt") as word_file:
            word_list = word_file.readlines()
            random_name += random.choice(word_list).strip()
            random_name += " "
            random_name += random.choice(word_list).strip()

        tip_smestaja = random.choice(tipovi_smestaja)
        tip_sobe = random.choice(tipovi_soba)
        internet = random.getrandbits(1)
        tv = random.getrandbits(1)
        klima = random.getrandbits(1)
        sobni_frizider=random.getrandbits(1)
        cena_prevoza = random.randint(100, 3000)
        kategorija = random.randint(1, 5)
        
        print(f"Kreiram smestaj \n\
            ime: {random_name}, \n\
            tip smestaja: {tip_smestaja.name}, \n\
            tip sobe: {tip_sobe.name}\n\
            internet: {internet}\n\
            tv: {tv}\n\
            klima: {klima}\n\
            sobni frizider: {sobni_frizider}\n\
            cena_prevoza: {cena_prevoza}\n\
            kategorija: {kategorija}\n\
            grad: {city.name}")

        smestaj_instances.append(
            Smestaj(
                name=random_name,
                kategorija=kategorija,
                internet=internet,
                tv=tv,
                klima=klima,
                sobni_frizider=sobni_frizider,
                cena_prevoza=cena_prevoza,
                grad=city,
                tip_smestaja=tip_smestaja,
                tip_sobe=tip_sobe,
            )
        )


    print("Cuvam generisane smestaje...")
    Smestaj.objects.bulk_create(smestaj_instances)

    return

class Migration(migrations.Migration):

    dependencies = [
        ("tripify", "0008_smestaj_tip_smestaja_smestaj_tip_sobe"),
    ]

    operations = [
        migrations.RunPython(napravi_smestaje),
    ]
