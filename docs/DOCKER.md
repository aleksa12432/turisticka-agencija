# Osnovne informacije
---

## Docker

Docker je open-source platforma za razvoj, dostavu i pokretanje aplikacija u kontejnerima. Kontejneri su izolovana okruženja koja sadrže sve potrebne zavisnosti i datoteke za pokretanje aplikacije, što omogućava jednostavno prenošenje aplikacije iz jednog okruženja u drugo.

+ Docker koristi Dockerfile datoteke kako bi opisao kako se aplikacija treba graditi i pokrenuti.
+ Docker koristi Docker Desktop kako bi upravljao kontejnerima i omogućio njihovo pokretanje na različitim platformama.
+ Kontejneri su izolovani od drugih kontejnera i od hosta, što omogućava veću sigurnost i pouzdanost aplikacija.
+ Docker Hub je javni registar za Docker kontejnere, gde možete pretraživati i deliti gotove kontejnere.
+ Docker se može koristiti za pokretanje aplikacija na lokalnom računaru ili na različitim cloud platformama poput Amazon Web Services, Google Cloud Platform ili Microsoft Azure.
+ Docker se često koristi u modernom softverskom razvoju, posebno za razvoj mikroservisa i kontinuiranu dostavu aplikacija. Kontejneri su takođe korisni za testiranje i razvoj na različitim platformama, kao i za osiguravanje da se aplikacije uviek pokreću u istom okruženju, bez obzira na to gde se izvode.
+ Korištćenje Docker-a može smanjiti vreme i napore koje programeri ulažu u postavljanje okruženja i razvoj aplikacija, što ga čini popularnim među programerima.

---
#### *Dockerfile*

    FROM python:3.8-slim-buster
Ova linija postavlja osnovnu sliku na Python 3.8 sa slim verzijom Debian "buster" operativnog sistema.

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

---

#### *docker-compose.yml*
     version: '3'
     services:
     web:
     build: .
     command: python manage.py runserver 0.0.0.0:8000
     volumes:
      - .:/app
     ports:
      - "8000:8000"
   
Ovaj kod predstavlja Docker Compose datoteku koja opisuje Docker uslugu nazvanu "web". Datoteka definiše kako se "web" usluga gradi, pokreće i konfiguriše.

Konkretno, ovaj kod opisuje Docker uslugu koja se gradi iz izvornog koda trenutnog direktorijuma gde se datoteka nalazi (naredba __'build: .__ '), a zatim pokreće Django aplikaciju s naredbom __'python manage.py runserver '__ na adresi __0.0.0.0:8000.__ Volumes se koriste za mapiranje lokalnih direktorijuma na direktorijume u Docker kontejneru, što omogućava promene u izvornom kodu bez potrebe ponovnog pokretanja kontejnera. Naredba ports mapira port 8000 iz Docker kontejnera na port 8000 lokalnog računala.

Ova Docker usluga bi se mogla pokrenuti s naredbom __docker-compose__ kako bi se pokrenula Django aplikacija. Ovaj primer je samo jedan od mnogih načina kako se može koristiti Docker Compose kako bi se pojednostavio postupak razvoja i razmeštaja aplikacija.

---


#### *requirements*

    Django
    django-extensions
    pydotplus
    pandas
    Pillow
    django-mathfilters
    requests

*Python django korišćene biblioteke*
