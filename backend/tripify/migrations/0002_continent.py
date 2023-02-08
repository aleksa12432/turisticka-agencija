from django.db import migrations

def add_continents(apps, schema_editor):
    Continent = apps.get_model('tripify', 'Continent')
    continents = [
        ("Africa",'images/africa.jpg'),
        ("Asia",'images/asia.jpg'),
        ("Europe",'images/europe.jpg'),
        ("North America",'images/namerica.jpg'),
        ("Oceania",'images/oceania.jpg'),
        ("South America",'images/samerica.jpg'),
    ]

    Continent.objects.bulk_create([Continent(name=name, image=image) for name, image in continents])

class Migration(migrations.Migration):

    dependencies = [
        ("tripify", "0001_initial"),
    ]


    operations = [
        migrations.RunPython(add_continents)
    ]
