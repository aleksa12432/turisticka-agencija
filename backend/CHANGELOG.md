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