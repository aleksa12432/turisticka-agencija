from django.test import TestCase
from tripify.models import Continent, Country, City, Tip_sobe, Tipovi_smestaja, Tip_prevoza, Smestaj, Aranzman, Smestaj_slika, Termin
from datetime import datetime


class ModelsTestCase(TestCase):
    
    def setUp(self):


        # Create an instance of your model
        test_kontinent=Continent.objects.create(name="Test_kontinent", image="test")
        test_drzava=Country.objects.create(name="Test_drzava", continent=test_kontinent)
        test_grad=City.objects.create(country=test_drzava, name="Test_grad")
        test_prevoz=Tip_prevoza.objects.create(name="Test_prevoz")
        test_tip_smestaj=Tipovi_smestaja.objects.create(name="Test_tip_smestaj")
        test_soba=Tip_sobe.objects.create(broj_ljudi=4, name="1/5")
        test_smestaj = Smestaj.objects.create(grad=test_grad, tip_smestaja=test_tip_smestaj, tip_sobe=test_soba, cena_prevoza=5000,internet=True,  kategorija=5, klima=False, name="Test_smestaj", sobni_frizider=True, tv=False)
        test_aranzman = Aranzman.objects.create(prevoz=test_prevoz, smestaj=test_tip_smestaj, cena=2000, duzina=8, naziv="Test_aranzman",  opis="test_opis", polazak=datetime.strptime('2022-03-11', '%Y-%m-%d'))
        test_smestaj_slika=Smestaj_slika.objects.create(smestaj=test_smestaj)
        test_termin=Termin.objects.create(aranzman=test_aranzman, smestaj=test_smestaj, vreme_stizanja=datetime.strptime('2022-06-15', '%Y-%m-%d'))

    def test_your_model(self):
        # Test that your model was created correctly
        print ("Testiram da li se kontinent uspesno kreira:")
        continent = Continent.objects.get(name="Test_kontinent")

        print ("Testiram da li se drzava uspesno kreira:")
        country = Country.objects.get(name="Test_drzava", continent=continent)

        print ("Testiram da li se grad uspesno kreira:")
        city = City.objects.get(country=country, name="Test_grad",)

        print ("Testiram da li se tip prevoza uspesno kreira:")
        tip_prevoza = Tip_prevoza.objects.get(name="Test_prevoz")

        print ("Testiram da li se tip smestaja uspesno kreira:")
        tip_smestaja = Tipovi_smestaja.objects.get(name="Test_tip_smestaj")

        print ("Testiram da li se tip sobe uspesno kreira:")
        tip_sobe = Tip_sobe.objects.get(broj_ljudi=4, name="1/5")

        print ("Testiram da li se smestaj uspesno kreira:")
        smestaj = Smestaj.objects.get(grad=city, tip_smestaja=tip_smestaja, tip_sobe=tip_sobe, cena_prevoza=5000, internet=True, kategorija=5, klima=False, name="Test_smestaj", sobni_frizider=True, tv=False)

        print ("Testiram da li se aranzman uspesno kreira:")
        aranzman = Aranzman.objects.get(prevoz=tip_prevoza, smestaj=tip_smestaja, cena=2000, duzina=8, naziv="Test_aranzman", opis="test_opis", polazak=datetime.strptime('2022-03-11', '%Y-%m-%d'))

        print ("Testiram da li se aranzman uspesno kreira:")
        smestaj_slika=Smestaj_slika.objects.get(smestaj=smestaj)

        print ("Testiram da li se termin uspesno kreira:")
        termin=Termin.objects.get(aranzman=aranzman, smestaj=smestaj)
    
        print ("Testiram da li se kontinent uspesno dodaje u bazu:")
        self.assertEqual(continent.name, "Test_kontinent")
        self.assertEqual(continent.image, "test")
        
        print ("Testiram da li se drzava uspesno dodaje u bazu:")
        self.assertEqual(country.name, "Test_drzava")
        self.assertEqual(country.continent, continent)

        print ("Testiram da li se grad uspesno dodaje u bazu:")
        self.assertEqual(city.country, country)
        self.assertEqual(city.name, "Test_grad")

        print ("Testiram da li je tip prevoza uspesno dodat u bazu:")
        self.assertEqual(tip_prevoza.name, "Test_prevoz")

        print ("Testiram da li je tip smestaja uspesno dodat u bazu:")
        self.assertEqual(tip_smestaja.name, "Test_tip_smestaj")
        
        print ("Testiram da li je tip sobe uspesno dodat u bazu:")
        self.assertEqual(tip_sobe.broj_ljudi, 4)
        self.assertEqual(tip_sobe.name, "1/5")

        print ("Testiram da li je smestaj uspesno dodat u bazu:")
        self.assertEqual(smestaj.grad,city)
        self.assertEqual(smestaj.tip_smestaja,tip_smestaja)
        self.assertEqual(smestaj.tip_sobe,tip_sobe)
        self.assertEqual(smestaj.cena_prevoza,5000)
        self.assertEqual(smestaj.internet,True)
        self.assertEqual(smestaj.kategorija,5)
        self.assertEqual(smestaj.klima,False)
        self.assertEqual(smestaj.name,"Test_smestaj")
        self.assertEqual(smestaj.sobni_frizider,True)
        self.assertEqual(smestaj.tv,False)

        print ("Testiram da li se aranzman uspesno dodaje u bazu:")
        self.assertEqual(aranzman.prevoz,tip_prevoza)
        self.assertEqual(aranzman.smestaj,tip_smestaja)
        self.assertEqual(aranzman.cena,2000)
        self.assertEqual(aranzman.duzina,8)
        self.assertEqual(aranzman.naziv,"Test_aranzman")
        self.assertEqual(aranzman.opis,"test_opis")
        self.assertEqual(aranzman.polazak,datetime.strptime('2022-03-11', '%Y-%m-%d'))

        print ("Testiram da li se smestaj slika uspesno dodaje u bazu:")
        self.assertEqual(smestaj_slika.smestaj,smestaj)


        print ("Testiram da li se termin uspesno dodaje u bazu:")
        self.assertEqual(termin.aranzman, aranzman)
        self.assertEqual(termin.smestaj, smestaj)

        continent.delete()
        country.delete()
        city.delete()
        tip_prevoza.delete()
        tip_smestaja.delete()
        tip_sobe.delete()
        smestaj.delete()
        aranzman.delete()
        smestaj_slika.delete()
        termin.delete()