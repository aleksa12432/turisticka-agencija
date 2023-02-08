from django.db import migrations
import pandas as pd
import requests
from google_images_search import GoogleImagesSearch
from PIL import Image
from io import BytesIO

BROJ_DRZAVA = 30
BROJ_GRADOVA = 90

API_KEY = 'AIzaSyBHzOoMnnAS_LtpfEzjkvPbVqC58qV-YKw'
CX = 'a6540a55c7e634a15'

def jednako(df, imekolone, br):
    grouped = df.groupby(imekolone)
    sampled = grouped.apply(lambda x: x.sample(br))

    return sampled

def add_countries_and_cities(apps, schema_editor):

    Continent = apps.get_model('tripify', 'Continent')
    Country = apps.get_model('tripify', 'Country')
    City = apps.get_model('tripify', 'City')

    # ucitavanje podataka u DataFrame
    dfCountries = pd.read_csv('./tripify/migrations/data/countries.csv')[["continent", "country"]]
    dfCities = pd.read_csv('./tripify/migrations/data/worldcities.csv')[["city", "country"]]

    # grupisemo gradove po drzavama
    grouped_cities = dfCities.groupby("country")

    # brojimo gradove po drzavama
    city_counts = grouped_cities.size().reset_index(name="city_count")

    # spajamo drzave sa brojem gradova
    merged_df = pd.merge(dfCountries, city_counts, on="country", how="left")

    # filtriramo drzave koje imaju manje od 3 gradova
    filtered_df = merged_df[merged_df["city_count"] >= 3].drop("city_count", axis=1)

    # uzimamo BROJ_DRZAVA/BROJ_KONTINENATA 
    # nasumicnih drzava sa jednakim brojem drzava po kontinentu
    countries = jednako(filtered_df, "continent", int(BROJ_DRZAVA/6))

    # uzimamo samo gradove cije su drzave u listi countries
    dfMergedCities = pd.merge(dfCities, countries, on='country')
    
    # uzimamo BROJ_GRADOVA/BROJ_DRZAVA gradova sa jednakim brojem
    # gradova po drzavi
    cities = jednako(dfMergedCities, "country", int(BROJ_GRADOVA/BROJ_DRZAVA))

    country_dict = countries.to_dict('records')
    cities_dict = cities.to_dict('records')

    # pravimo niz sa svim drzavama da bi iskoristili bulk create
    country_instances = [Country(
        name=record['country'],
        # uzimamo kontinent pronalazenjem
        continent=Continent.objects.get(name=record['continent']),
    ) for record in country_dict]

    # pravimo drzave
    Country.objects.bulk_create(country_instances)

    city_instances = []

    print(cities_dict)


    for city in cities_dict:
        city_name = city["city"]
        country_name = city["country"]
        gis = GoogleImagesSearch(API_KEY, CX) # ucitavamo google images search api sa datim api_key i CX
        search_params = {
            'q': city_name, # trazimo ime grada na google images
            'num': 1 # uzimamo samo 1 sliku
        }
        # print(search_params)
        gis.search(search_params=search_params) # pretrazujemo sa datim parametrima
        result = gis.results()[0] # uzimamo prvi rezultat pretrage
        url = result.url # cuvamo url

        response = requests.get(url) # pomocu requests biblioteke cuvamo sliku kao response

        img = Image.open(BytesIO(response.content)) # pravimo sliku od response-a
        img.thumbnail((400, 300)) # rescale-ujemo na 400x300
        output_buffer = BytesIO()

        img.save(output_buffer, format='webp') # upisujemo sliku u output_buffer u webp format

        # dodajemo grad na listu
        city_instances.append(City( 
            name=city_name, 
            country=Country.objects.get(name=country_name),
            image=File(output_buffer, name='{}.webp'.format(city_name)))) # django ima da handluje upload fajla
        
    City.objects.bulk_create(city_instances) # pravimo gradove


class Migration(migrations.Migration):

    dependencies = [
        ("tripify", "0002_continent"),
    ]


    operations = [
        migrations.RunPython(add_countries_and_cities)
    ]
