# 12. februar 2023.

### tripify/settings.py:
- Dodato podesavanje za proveravanje testnog okruzenja
- Baza prebacena sa MariaDB/MySQL na SQLite __ubrzalo pretragu x2__

### tripify/templates/*.html:
- Popravljen prikaz slika na novim generacijama

### tripify/templates/vacation.html:
- Namesten prikaz pojedinacnih aranzmana

### tripify/templates/home.html:
- Uklonjen prikaz gradova

### tripify/templates/cities.html:
- Prikaz gradova prebacen

### tripify/templates/city.html:
- Prikazuje sve aranzmane koji prolaze kroz taj grad

### tripify/settings_test.py:
- Podesavanja koja se koriste pri testiranju

### tripify/migrations/0005_tipovi_smestaja_tipovi_sobe.py:
- Prevedeni na engleski jezik

### tripify/migrations/0006_tipovi_prevoza.py:
- Prevedeni na engleski jezik

### tripify/migrations/0003_countries_cities.py:
- Proverava ako je testno okruzenje, u tom slucaju ne upotrebljava bing image search
- Try catch block proverava ako je slika nadjena uopste, ako nije koristimo placeholder image

### tripify/templates/package.html:
- sada pretraga i stranicenje radi u potpunosti
- dodato i biranje broja rezultata po strani

### tripify/models.py:
- dodate \_\_str\_\_ metode za modele zbog boljeg prikaza na admin stranici

# 11. februar 2023. - inicijalizacija podataka zavrsena!

### tripify/migrations/0013_aranzmani.py:
- Generise aranzmane i termine po specifikaciji

### tripify/admin.py:
- U admin prikazu dodate ostale tabele

### tripify/views.py:
- Dodati prikazi 3 najskorija aranzmana
- vacation sada prima id i prikazuje aranzman sa tim id-em

### tripify/settings.py:
- USE_TZ postavljen na false

# 10. februar 2023.

### tripify/migrations/0010_slike_smestaja.py:
- Unosi slike smestaja

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