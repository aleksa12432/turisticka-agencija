# 09. februar 2023.

### tripify/models.py:
- prepravljen upload_to na tripify/static
- dodato jos modela

### tripify/migrations/0002_continent.py:
- Dodat verbose

### tripify/migrations/0005_tipovi_smestaja_tipovi_sobe.py:
- Unosi tipove smestaja i tipove soba

### tripify/migrations/0006_tipovi_prevoza.py:
- Unosi tipove prevoza

### tripify/migrations/0009_smestaji.py:
- Unosi smestaje (3 po gradu - config na vrhu)

### resources/slike_smestaja/:
- Preuzeto 30 slika za smestaje

### tripify/migrations/0003_countries_cities.py:
- Google images api limitira na samo 100 requesta dnevno, nedovoljno za testiranje
- Prelazimo na bing koji dozvoljava 1000 mesecno, 3 req/s
- __RADI!!!__ 🙏
- Dodat verbose
- Prepravljene pretrage na "{imepretrage} city" za sledece pokretanje


# 08. februar 2023.

### tripify/models.py:
- Rekonstruisani svi modeli tako da se poklapaju sa [specifikacijom](/SPECIFIKACIJA.md)

### tripify/migrations/0002_continent.py:
- Napravljena pocetna migracija za kontinenta

### tripify/migrations/0003_countries_cities.py:
- Napravljena migracija za gradove i drzave, slike se ucitavaju pomocu google search API, pretragom grada, konvertuju sliku u 400x300 webp format

### tripify/admin.py:
- Sada ucitava samo tabele koje su potrebne adminu da edituje

### google images api me limitirao, moram sutra da dodajem slike :(

# 07. februar 2023.

### css/home.css:
- .box img izmenjen u object-fit: cover da se ne bi sirila slika

### index:
- Kontinenti i putanje slika kontinenata se sada ucitavaju iz baze

# 06. februar 2023. - pocetak

### Projekat:
- Kreiran backend

### tripify/models.py:
- Kreiran models.py od baze sa svim modelima

### tripify/admin.py:
- Kreiran admin.py koji importuje modele u admin stranicu

### tripify/urls.py:
- Kreiran urls.py koji cuva prikazane urlove na stranici

### tripify/views.py:
- Kreiran views.py koji cuva prikaze stranica

### templates/*.html:
- Pretvoreni svi html fajlovi u django template format

### static/:
- Staticki fajlovi se nalaze u ovom direktorijumu