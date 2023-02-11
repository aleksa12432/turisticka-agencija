from django.db import migrations
import os
import random
from PIL import Image
from io import BytesIO
from django.core.files import File

DIREKTORIJUM_SLIKA = 'resources/smestaj_slike'

def add_slike_smestaja(apps, schema_editor):

    Smestaj_slika = apps.get_model('tripify', 'Smestaj_slika')
    Smestaj = apps.get_model('tripify', 'Smestaj')

    smestaji = Smestaj.objects.all()

    slike = os.listdir(DIREKTORIJUM_SLIKA)

    print("Ucitavam slike smestaja...")
    smestaji_slike_instances = []

    for smestaj in smestaji:

        print(f"Smestaj: {smestaj.name}")
        
        broj_slika = random.randint(1,6)

        print(f"Broj slika: {broj_slika}")

        izabrane_slike = random.sample(slike, broj_slika)

        print(f"Izabrane slike: {izabrane_slike}")

        for slika, index in zip(izabrane_slike, range(broj_slika)):

            print(f"Dodajem sliku: {slika} za smestaj {smestaj.name}")

            img = Image.open(DIREKTORIJUM_SLIKA + "/" + slika)

            img.thumbnail((400, 300), Image.Resampling.LANCZOS) # rescale-ujemo na 400x300

            output_buffer = BytesIO()

            img.save(output_buffer, format='webp') # upisujemo sliku u output_buffer u webp format

            print(f"Cuvam sliku {smestaj.name.replace(' ', '')}{index}.webp")
            
            image_file = File(output_buffer, 
            name=f'{smestaj.name.replace(" ", "")}{index}.webp')

            smestaji_slike_instances.append(Smestaj_slika(
                img=image_file,
                smestaj=smestaj,
            ))
    
    print("Gotovo ucitavanje slika smestaja, popunjavam u bazi...")

    Smestaj_slika.objects.bulk_create(smestaji_slike_instances) # pravimo gradove

class Migration(migrations.Migration):

    dependencies = [
        ("tripify", "0009_smestaji"),
    ]

    operations = [
        migrations.RunPython(add_slike_smestaja),
    ]
