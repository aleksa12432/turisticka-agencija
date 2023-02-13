from django.db import migrations
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.conf import settings

BROJ_DRZAVA = 30
BROJ_GRADOVA = 90

SUBSCRIPTION_KEY = "6b0f819c8b8d44828dcac4141f408a7c"
SEARCH_URL = "https://api.bing.microsoft.com/v7.0/images/search"

def jednako(df, imekolone, br):
    grouped = df.groupby(imekolone)
    sampled = grouped.apply(lambda x: x.sample(br))

    return sampled

# prima string search_term, vraca url pronadjene slike
def pronadji_sliku(search_term):

    print(f"Trazim sliku za {search_term}...")

    if settings.MIGRATIONS_RUN_AS_TEST:
        return "https://www.slntechnologies.com/wp-content/uploads/2017/08/ef3-placeholder-image.jpg"

    params = {
        "q": search_term, 
        "count": 1
    }

    headers = {"Ocp-Apim-Subscription-Key" : SUBSCRIPTION_KEY}

    response = requests.get(SEARCH_URL, headers=headers, params=params)
    response.raise_for_status()

    search_results = response.json()

    try: 
        img_url = search_results["value"][0]["thumbnailUrl"] # ako ne pronadje sliku
    except:
        img_url = "https://www.slntechnologies.com/wp-content/uploads/2017/08/ef3-placeholder-image.jpg"
    
    print(f"Pronadjena slika: {img_url}")
    
    return img_url

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

    print(f"Biram {BROJ_DRZAVA} nasumicnih drzava...")

    # uzimamo BROJ_DRZAVA/BROJ_KONTINENATA 
    # nasumicnih drzava sa jednakim brojem drzava po kontinentu
    countries = jednako(filtered_df, "continent", int(BROJ_DRZAVA/6))

    # uzimamo samo gradove cije su drzave u listi countries
    dfMergedCities = pd.merge(dfCities, countries, on='country')

    print(f"Biram {BROJ_GRADOVA} nasumicnih gradova...")
    
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

    print("Popunjavam drzave...")

    # pravimo drzave
    Country.objects.bulk_create(country_instances)

    city_instances = []

    print("Pocinjem popunjavanje gradova sa slikama...")

    for city in cities_dict:
        city_name = city["city"]
        country_name = city["country"]

        print(f"Ucitavam: {country_name} - {city_name}")

        url = pronadji_sliku(city_name)

        image_data = requests.get(url) # pomocu requests biblioteke cuvamo sliku kao response

        img = Image.open(BytesIO(image_data.content)) # pravimo sliku od response-a

        img.thumbnail((400, 300), Image.Resampling.LANCZOS) # rescale-ujemo na 400x300

        output_buffer = BytesIO()

        img.save(output_buffer, format='webp') # upisujemo sliku u output_buffer u webp format
        
        image_file = File(output_buffer, name=f'{city_name}.webp')

        # dodajemo grad na listu
        city_instances.append(City( 
            name=city_name, 
            country=Country.objects.get(name=country_name),
            image=image_file # django ima da handluje upload fajla
        )) 

    print("Popunjavam gradove...")

    # raise NotImplementedError("Nije gotovo!")
    City.objects.bulk_create(city_instances) # pravimo gradove


class Migration(migrations.Migration):

    dependencies = [
        ("tripify", "0002_continent"),
    ]

    operations = [
        migrations.RunPython(add_countries_and_cities)
    ]
