from django.test import TestCase
from tripify.models import Continent, Country, City, Tip_sobe, Tipovi_smestaja, Tip_prevoza, Smestaj, Aranzman, Smestaj_slika, Termin
from datetime import datetime

class GenerationTestCase(TestCase):
    
    def setUp(self):
        # Create an instance of your model
        return

    def test_your_model(self):
        continents = Continent.objects.all()
        countries = Country.objects.all()
        cities = City.objects.all()
        tipovi_prevoza = Tip_prevoza.objects.all()
        tipovi_smestaja = Tipovi_smestaja.objects.all()
        tipovi_sobe = Tip_sobe.objects.all()
        smestaji = Smestaj.objects.all()
        aranzmani_novi= Aranzman.objects.filter(polazak__gt=datetime.today())
        aranzmani_stari= Aranzman.objects.filter(polazak__lt=datetime.today())
        smestaj_slike=Smestaj_slika.objects.all()
        termini=Termin.objects.all()

        print ("Testiram da li je broj kontinenata 6:")
        self.assertEqual(len(continents), 6)

        print ("Testiram da li je ukupan broj drzava jednak ili veci od 30:")
        self.assertGreaterEqual(len(countries), 30)

        print ("Testiram da li je ukupan broj gradova jednak ili veci od 90:")
        self.assertGreaterEqual(len(cities), 90)

        print ("Testiram da li je broj tipova prevoza 5:")
        self.assertEqual(len(tipovi_prevoza), 5)

        print ("Testiram da li je broj tipova smestaja 2:")
        self.assertEqual(len(tipovi_smestaja), 2)

        print ("Testiram da li je broj tipova sobe 6:")
        self.assertEqual(len(tipovi_sobe), 6)

        print ("Testiram da li je broj smestaja jednak ili veci od 270:")
        self.assertGreaterEqual(len(smestaji), 270)

        print ("Testiram da li je broj novih aranzmana jednak ili veci od 50 000:")
        self.assertGreaterEqual(len(aranzmani_novi), 50000)

        print ("Testiram da li je broj isteklih aranzmana jednak ili veci od 10 000:")
        self.assertGreaterEqual(len(aranzmani_stari), 10000)

        print ("Testiram da li je broj smestaj slika izmedju 270 i 1620:")
        self.assertGreaterEqual(len(smestaj_slike), 270)
        self.assertLessEqual(len(smestaj_slike), 1620)

        print ("Testiram da li je broj termina veci od 60000:")
        self.assertGreaterEqual(len(termini), 60000)