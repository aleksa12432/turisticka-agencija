# Osnovne informacije
---

## Docker


#### *Dockerfile*

    FROM python:3.8-slim-buster
Ova linija postavlja osnovnu sliku na Python 3.8 sa slim verzijom Debiijan "buster" operativnog sistema.

     WORKDIR /app
Ova linija postavlja radni direktorijum na /app unutar kontejnera.

     COPY requirements.txt .
     RUN pip install -r requirements.txt
Ove linije kopiraju requirements.txt datoteku u kontejner i instaliraju sve neophodne zavisnosti projekta pomoću pip alata.

     COPY . .    
Ova linija kopira sve datoteke iz trenutnog direktorijuma (u kojem se nalazi Dockerfile) u direktorijum /app unutar kontejnera.

     ENV PYTHONUNBUFFERED 1   
Ova linija postavlja varijablu okruženja koja sprečava keširanje standardnog izlaza.

     RUN python manage.py test --settings=tripify.settings_test
  
Ova linija izvršava testove za Django aplikaciju u kontejneru, koristeći tripify.settings_test podešavanja.

    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
Ova linija pokreće Django aplikaciju unutar kontejnera. Aplikacija će biti pokrenuta na adresi 0.0.0.0:8000.


### *requirements*
     Django
     django-extensions
     pydotplus
     pandas
     Pillow
     django-mathfilters
     requests
    
    *Python django biblioteke*
