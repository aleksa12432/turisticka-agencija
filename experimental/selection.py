import pandas as pd
import numpy as np

BROJ_DRZAVA = 30
BROJ_GRADOVA = 90

def jednako(df, imekolone, br):
    grouped = df.groupby(imekolone)
    sampled = grouped.apply(lambda x: x.sample(br))

    return sampled


def main():
    # ucitavanje podataka u DataFrame
    dfCountries = pd.read_csv('./countries.csv')[["continent", "country"]]
    dfCities = pd.read_csv('./worldcities.csv')[["city", "country"]]

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

    print(cities)

if __name__ == '__main__':
    main()