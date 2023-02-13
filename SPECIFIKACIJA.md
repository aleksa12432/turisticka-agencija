# Projekat treba da ima:

### Aranzmani:
- podrazumevaju:
    - prevoz
        - autobusom
        - avionom
        - krstarenje
        - vozom
        - samostalni prevoz
    - smestaj
        - hotelski
        - bungalovi
    - program putovanja
        - termin
        - lokacija
        - detaljan opis programa i fakultativnih aktivnosti
            - izleti
            - sportske aktivnosti
            - zurke
- Prvo aktivni pa prosli
- Detaljan pregled:
    - naziv aranzmana
    - lokacija (ili vise njih)
    - slika lokacije na koju se putuje
        - ako je vise lokacija, prikazuje se ona sa najvise dana u lokaciji
    - cena i tip prevoza
    - opis smestaja
        - ime smestajnog objekta
        - tip smestaja u sobi
        - kategorija smestaja
        - dodatni detalji
            - internet
            - tv
            - klima
            - sobni frizider
            - do 6 fotografija smestaja
    - detaljan program putovanja
        - ako traje 6 dana, za svaki dan je dostupan program
    - napomene
        - detalji poput napomena u vezi sa osiguranjem
        - detalji prevoza
        - napomene u vezi sa viznim i pasoskim protokolom
        - ogranicenja
            - prtljaga
            - rasporeda sedenja
            - nacina placanja
- Rezervacija
    - korisnik moze da rezervise aranzman
        - unosi
            - ime
            - prezime
            - kontakt telefon
            - email
            - nacin placanja
            - broj osoba koje putuju (odrasli + dece)
            - komentar (npr posebni zahtevi)
    - ne moze da rezervise aranzman koji je prosao
- u pregledu u pretrazi sadrzi:
    - naziv
    - destinaciju
    - sliku
    - termin putovanja (datum + broj dana) 
    - cenu 
    - tip prevoza
- stranicenje 
    - 25
    - 50 - default
    - 100
    - 200
- ista destinacija ima istu sliku
    

### Pretraga:
- po nazivu
- po kontinentu
- po tipu prevoza
- po kalendaru
    - ako je navedeno od-do prikazuje samo aranzmane sa tacnim datumima
    - ako je navedeno samo od - prikazuje sva putovanja sa tim pocetnim datumom, bez obzira na trajanje

### Inicijalizacija
- 60k ponuda
    - 50k aktuelnih
    - 10k proslih
- nasumicno generisani
    - normalna raspodela
- ime aranzmana je jedinstveno - (npr Rim novembar 2022)
- drzave i gradovi su realni podaci
    - 30 drzava
    - 90 gradova
- opisi:
    - prvo:
        - "polazak sa {perona}/{aerodroma} u {vreme}
        - lorem ipsum
        - dolazak u {ime polazne lokacije} u {jutarnjim}/{prepodnevnim}/{popodnevnim}/{vecernjim} satima
- smestaj
    - fotografije
        - do 6 po smestaju
        - rasporedjivati iz skupa od 30 fotografija sa interneta
    - ostali detalji smestaja
        - cena prevoza [100, 3000]e
        - tip prevoza
        - tip smestaja u sobi
            - 1/1
            - 1/2
            - 1/3
            - 1/2+1
            - 1/3+1
            - 1/4
        - kategorija smestaja
            - int [1,5]
        - ima/nema:
            - internet
            - TV
            - klima (AC)
            - sobni frizider