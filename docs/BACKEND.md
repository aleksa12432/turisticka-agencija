# Osnovne informacije:
### Upotrebljene biblioteke/framework-ovi:

#### Python server Django
- Upotrebljen jer je jedan od najpopularnijih web framework-ova na svetu, omogucava brzo i efikasnu izgradnju robustnih web aplikacija.

- Poseduje znacajne prednosti poput visokog stepena sigurnosti, modularne arhitekture, jednostavnosti i fleksibilnosti.

- Podrzava potpuno objektno orijentisano programiranje, sto omogucava lakocu razvoja i skalabilnosti aplikacije. 
- Ima bogatu dokumentaciju i aktivnu zajednicu koja je spremna da pomogne pri razvoju.

- Koriscenjem Django-a, brzo i efikasno je razvijena web aplikacija sa robustnim funkcionalnostima.

- Django omogucava fokusiranje paznje na logiku aplikacije, umesto na neke od tehnickih aspekata izgradnje web stranice.

- Ukratko - __izabran zbog funkcionalnosti, jednostavnosti i efikasnosti u razvoju web aplikacije__

#### Pandas
- Upotrebljen za obradu podataka.
- Jedan od najpopularnijih biblioteka za rad sa podacima u Python programskom jeziku.
- Omogucava brzo i efikasno ucitavanje, obradu i analizu velikih kolicina podataka.
- Pruza mnostvo funkcija za manipulaciju i obradu podataka, ukljucujuci agregaciju, filtriranje, grupisanje i pivotiranje tabela.
- Podrzava rad sa razlicitim formatima podataka, ukljucujuci CSV, Excel, SQL i druge formate.
- U projektu konkretno (backend/tripify/0003_countries_cities) izabran za generaciju gradova i drzava, pomogao kod odabira gradova i drzava u svetu, sa jednakom raspodelom

#### django-extensions:
- Upotrebljen kao dodatak Django web framework-u
- Upotrebljen u generaciji [slike modela baze](../db/tripify_models.png)

#### Pillow:
- Pruza sirok spektar funkcionalnosti za rad sa slikama, ukljucujuci citanje, izmenu i cuvanje slika u razlicitim formatima.
- Upotrebljen u konverziji preuzetih slika u efikasan format (webp 400x300)

#### django-mathfilters:
- Upotrebljen kao dodatak Django web framework-u
- Upotrebljen za racunicu jednostavnih matematickih izraza u [template fajlovima](../backend/tripify/templates/package.html) radi ubrzavanja stranicenja

#### requests:
- Upotrebljen za pravljenje web request-ova, konkretno preuzimanje slika i komuniciranje sa [Bing Image Search API](https://www.microsoft.com/en-us/bing/apis/bing-image-search-api)

#### pydotplus:
- Upotrebljen zbog requirement-a za generaciju slika pomocu django-extensions

### Struktura fajlova:

```bash
backend
├── CHANGELOG.md 
├── manage.py 
├── README.md 
├── resources 
│   ├── smestaj_slike 
│   └── smestaj_tekst.txt
├── tripify
│   ├── admin.py
│   ├── asgi.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_continent.py
│   │   ├── 0003_countries_cities.py
│   │   ├── 0004_tip_prevoza_tip_sobe_tipovi_smestaja.py
│   │   ├── 0005_tipovi_smestaja_tipovi_sobe.py
│   │   ├── 0006_tipovi_prevoza.py
│   │   ├── 0007_smestaj_smestaj_slika.py
│   │   ├── 0008_smestaj_tip_smestaja_smestaj_tip_sobe.py
│   │   ├── 0009_smestaji.py
│   │   ├── 0010_slike_smestaja.py
│   │   ├── 0011_aranzman_termin.py
│   │   ├── 0012_alter_aranzman_naziv.py
│   │   ├── 0013_aranzmani.py
│   │   └── data
│   │       ├── countries.csv
│   │       └── worldcities.csv
│   ├── models.py
│   ├── settings.py
│   ├── settings_test.py
│   ├── static
│   │   ├── css
│   │   │   ├── about.css
│   │   │   ├── book.css
│   │   │   ├── home.css
│   │   │   ├── package.css
│   │   │   ├── responsive.css
│   │   │   ├── style.css
│   │   │   └── vacation.css
│   │   ├── images
│   │   ├── js
│   │   │   └── script.js
│   │   └── smestaji
│   ├── templates
│   │   ├── about.html
│   │   ├── __base.html
│   │   ├── book.html
│   │   ├── cities.html
│   │   ├── city.html
│   │   ├── home.html
│   │   ├── package.html
│   │   └── vacation.html
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
└── tripify.db
```

| Direktorijum/Fajl                                                | Upotreba                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CHANGELOG.md                                                     | Detaljni opisi promena                                                                                                                                                                                                                                                                                                                |
| manage.py                                                        | utility koji dolazi uz django projekat - pokrece sve - testove, migracije, server                                                                                                                                                                                                                                                     |
| README.md                                                        | README                                                                                                                                                                                                                                                                                                                                |
| resources/                                                       | resursi za izgradnju/migraciju                                                                                                                                                                                                                                                                                                        |
| resources/smestaj_slike/                                         | slike upotrebljene za generaciju smestaja                                                                                                                                                                                                                                                                                             |
| resources/smestaj_tekst.txt                                      | tekst fajl upotrebljen za generaciju imena smestaja                                                                                                                                                                                                                                                                                   |
| tripify/                                                          | direktorijum "tripify" aplikacije u django okruzenju                                                                                                                                                                                                                                                                                  |
| tripify/admin.py                                                 | fajl koji povezuje admin funkcionalnosti u django okruzenju                                                                                                                                                                                                                                                                           |
| tripify/asgi.py                                                  | fajl koji definise ASGI aplikaciju - standardni interfejs kojim Python web aplikacije komuniciraju sa web serverima                                                                                                                                                                                                                   |
| tripify/migrations                                               | direktorijum koji sadrzi migracije - pokrecu se pri prvom pokretanju servera - konfigurisu bazu i inicijalizuju podatke                                                                                                                                                                                                               |
| tripify/migrations/0001_initial.py                               | pravi tabele Continent, Country i City                                                                                                                                                                                                                                                                                                |
| tripify/migrations/0002_continent.py                             | inicijalizuje kontinente zadate po specifikaciji                                                                                                                                                                                                                                                                                      |
| tripify/migrations/0003_countries_cities.py                      | inicijalizuje drzave i gradove po BROJ_DRZAVA i BROJ_GRADOVA konstantama, takodje sadrzi SUBSCRIPTION_KEY u kom se nalazi Bing API key - ovaj fajl pretrazuje pomocu Bing API slike gradova, u slucaju da je parametar MIGRATIONS_RUN_AS_TEST postavljen na True - umesto ucitavanja slika preko Bing API - koristi placeholder sliku |
| tripify/migrations/0004_tip_prevoza_tip_sobe_tipovi_smestaja.py  | pravi tabele Tip_prevoza, Tip_sobe i Tipovi_smestaja                                                                                                                                                                                                                                                                                  |
| tripify/migrations/0005_tipovi_smestaja_tipovi_sobe.py           | inicijalizuje tipove smestaja i tipove sobe zadate po specifikaciji                                                                                                                                                                                                                                                                   |
| tripify/migrations/0006_tipovi_prevoza.py                        | inicijalizuje tipove prevoza zadate po specifikaciji                                                                                                                                                                                                                                                                                  |
| tripify/migrations/0007_smestaj_smestaj_slika.py                 | pravi tabele Smestaj i Smestaj_slika                                                                                                                                                                                                                                                                                                  |
| tripify/migrations/0008_smestaj_tip_smestaja_smestaj_tip_sobe.py | dodaje kolone tip_smestaja i tip_sobe na Smestaj                                                                                                                                                                                                                                                                                      |
| tripify/migrations/0009_smestaji.py                              | inicijalizuje BROJ_SMESTAJA_PO_GRADU smestaja za svaki grad, imena generise iz resources/smestaj_slike.txt fajla                                                                                                                                                                                                                      |
| tripify/migrations/0010_slike_smestaja.py                        | inicijalizuje slike smestaja po specifikaciji, nasumican broj i nasumicnu sliku iz resources/smestaj_slike/ direktorijuma - resize-uje ih na 400x300 i konvertuje u webp prilikom cuvanja                                                                                                                                             |
| tripify/migrations/0011_aranzman_termin.py                       | pravi tabele Aranzman i Termin                                                                                                                                                                                                                                                                                                        |
| tripify/migrations/0012_alter_aranzman_naziv.py                  | smanjuje velicinu kolone name na 255 - mariadb ne prihvata unique kolone duze od 255                                                                                                                                                                                                                                                  |
| tripify/migrations/0013_aranzmani.py                             | inicijalizuje aranzmane sa terminima - BROJ_PROSLIH_ARANZMANA zastarelih aranzmana i BROJ_AKTUELNIH_ARANZMANA novih aranzmana; aranzman moze da ima MAX_LOKACIJA_PO_ARANZMANU gradova posecenih u jednom aranzmanu                                                                                                                    |
| tripify/migrations/data/                                         | direktorijum sa podacima koriscenim u generaciji                                                                                                                                                                                                                                                                                      |
| tripify/migrations/data/countries.csv                            | cuva podatke drzava                                                                                                                                                                                                                                                                                                                   |
| tripify/migrations/data/worldcities.csv                          | cuva podatke gradova                                                                                                                                                                                                                                                                                                                  |
| tripify/models.py                                                | sadrzi sve modele (tabele) koriscene u aplikaciji                                                                                                                                                                                                                                                                                     |
| tripify/settings.py                                              | opsta podesavanja djanga                                                                                                                                                                                                                                                                                                              |
| tripify/settings_test.py                                         | podesavanja djanga koja se koriste pri testiranju                                                                                                                                                                                                                                                                                     |
| tripify/static/                                                  | cuva sve staticke fajlove                                                                                                                                                                                                                                                                                                             |
| tripify/static/css/                                              | cuva css stil fajlove                                                                                                                                                                                                                                                                                                                 |
| tripify/static/images/                                           | cuva pojedine slike                                                                                                                                                                                                                                                                                                                   |
| tripify/static/js/                                               | cuva javascript fajlove                                                                                                                                                                                                                                                                                                               |
| tripify/templates/                                               | cuva django template fajlove - sluze za prikaz poput html fajlova sa dodatnom sintaksom                                                                                                                                                                                                                                               |
| tripify/templates/about.html                                     | template fajl prikaza about stranice                                                                                                                                                                                                                                                                                                  |
| tripify/templates/__base.html                                    | template fajl koji je baza za ostale template fajlove - sadrzi head, header (navbar) i footer                                                                                                                                                                                                                                         |
| tripify/templates/book.html                                      | template fajl koji prikazuje book stranicu                                                                                                                                                                                                                                                                                            |
| tripify/templates/cities.html                                    | template fajl koji prikazuje gradove na osnovu date drzave                                                                                                                                                                                                                                                                            |
| tripify/templates/city.html                                      | template fajl koji prikazuje aranzmane u pojedinom gradu                                                                                                                                                                                                                                                                              |
| tripify/templates/home.html                                      | template fajl koji prikazuje pocetnu stranu                                                                                                                                                                                                                                                                                           |
| tripify/templates/package.html                                   | template fajl koji prikazuje sve aranzmane i pretragu                                                                                                                                                                                                                                                                                 |
| tripify/templates/vacation.html                                  | template fajl koji prikazuje detaljno aranzman                                                                                                                                                                                                                                                                                        |
| tripify/urls.py                                                  | fajl koji definise upotrebljive url-ove u django framework-u i kako se prikazuju                                                                                                                                                                                                                                                      |
| tripify/views.py                                                 | fajl koji pokrece prikaze (template fajlove) i pozadinsku logiku (npr get requestove), ucitava sve podatke neophodne i passuje template fajlu                                                                                                                                                                                         |
| tripify/wsgi.py                                                  | fajl koji sluzi kao entry point za python web aplikacije preko WSGI (Web Server Gateway Interface) protokola                                                                                                                                                                                                                          |
| tripify.db                                                       | sqlite3 baza upotrebljena u projektu                                                                                                                                                                                                                                                                                                  |