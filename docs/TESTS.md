# QA TESTIRANJE

## Uvod:

Ovaj dokument pruža rezime svih QA testova obavljenih za web aplikaciju Tripify koristeći Django okvir ze testiranje. Naš cilj je da osiguramo da je sva funkcionalnost aplikacije testirana kako bi se sprečile moguće greške prilikom korišćenja.

## Okruženje u kome je testiranje izvršeno:

- Python verzija 3.10.10
- Django verzija 4.1.6
- django-extensions verzija 3.2.1
- Pandas verzija 1.5.3
- Pillow verzija 9.4.0
- requests verzija 2.28.2

## Strategija testiranja

Korišćena je Django TestCase klasa za testiranje svih pogleda i modela u aplikaciji. TestCase klasa pruža izolovano okruženje za pokretanje testova, što pomaže u osiguravanju da su testovi dosledni i pouzdani.

## Struktura direktorijuma

| Direktorijum/Fajl                    | Upotreba                                                                              |
|--------------------------------------|---------------------------------------------------------------------------------------|
| tests/test_models.py                 | Fajl u kome je omogućeno testiranje pojedinačnih klasa modela.                        |
| tests/test_generation.py             | Fajl u kome se testira da li su svi podaci generisani po specifikaciji                |
| tests/test_views.py                  | Fajl u kome je omogućeno testiranje HTTP putanje                                      |
| tests/test_registration_login_and_book.py | Fajl u kome se testira da li su registracija, prijava korisnika i rezervacija validni |

## Test Cases

### 1. Models

`test_models.py` omogućava proces testiranja pojedinačnih klasa modela. To uključuje stvaranje primera klase modela, tvrdnju da atributi i metode modela rade kako se očekuje i osiguranje da model može da interaguje sa ostalim delovima aplikacije kako je potrebno.

### 2. Generation

`test_generation.py` proverava da li su svi podaci generisani kako je navedeno u specifikaciji. Ovo ukljucuje sumiranje svih instanci odnosno redova u tabeli i uporedjivanje sa njihovim očekivanim i potrebnim brojem pomoću ugradjene `assert` funkcije.

### 3. Views

`test_views.py` omogućava testiranje pojedinačnih funkcija prikaza. To obično uključuje slanje HTTP zahteva prikazu, ispitivanje odgovora koji vraća prikaz i tvrdnju da odgovor sadrži ispravne podatke i ima odgovarajući HTTP statusni kod

### 4. Registration, login and book

`test_registration_login_and_book.py` sadrži automatizovane testove za funkcionalnosti registracije, prijave i zakazivanja u našoj web aplikaciji. Testovi su osmišljeni da bi se osiguralo da je proces registracije i prijave funkcionalan i da korisnici mogu uspešno da zakazuju termine nakon što se prijave.

#### Testovi registracje

Testovi registracije su definisani u funkciji `test_0_register()`, koja koristi klasu Client da bi simulirala HTTP zahteve i proverila odgovor servera. Za svaki test slučaj, funkcija šalje POST zahtev na endpoint registracije, pružajući potrebne podatke. Zatim proverava da je odgovor servera očekivan, potvrđujući da je registracija bila uspešna ili da su vraćene odgovarajuće greške.

#### Testovi prijave i zakazivanja

Testovi prijave i zakazivanja su definisani u funkciji `test_1_login_book()`. Funkcija proverava da li je korisnik uspešno prijavljen, pristupajući potrebnim stranicama koje zahtevaju prijavljivanje, kao što je stranica za zakazivanje. Jedna od ključnih funkcionalnosti u našoj Django aplikaciji je mogućnost zakazivanja termina. Kako bi se osiguralo da ova funkcionalnost radi besprekorno, potrebno je napisati i izvršiti odgovarajuće testove. Ovi testovi osiguravaju da da korisnici mogu efikasno da zakazuju i otkazuju svoje termine.

## Rezultat testiranja

Svi testovi su uspešno prošli. Nisu otkriveni nikakvi problemi ili greške tokom testiranja.

## Zaključak

Temeljno testiranje je neophodno za osiguravanje kvaliteta i stabilnosti aplikacije. Korišćenjem Django TestCase klase, možemo biti sigurni da su sve funkcionalnosti aplikacije testirane i da je aplikacija spremna za korišćenje od strane krajnjih korisnika.

