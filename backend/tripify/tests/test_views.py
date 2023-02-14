from django.test import TestCase
from tripify.models import Aranzman, Continent, City

class MyViewTestCase(TestCase):
    def test_my_view(self):
        print ("Testiram pristup admin stranici:")
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)

        print ("Testiram pristup index stranici:")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        print ("Testiram pristup about stranici:")
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

        print ("Testiram pristup package stranici:")
        response = self.client.get('/package/')
        self.assertEqual(response.status_code, 200)

        print ("Testiram pristup vacation stranici:")
        response = self.client.get('/vacation/')
        self.assertEqual(response.status_code, 400)

        aranzman = Aranzman.objects.first()

        print ("Testiram pristup vacation stranici sa datim id-em:")
        response = self.client.get(f'/vacation/?id={aranzman.pk}')
        self.assertEqual(response.status_code, 200)

        print ("Testiram pristup cities stranici:")
        response = self.client.get('/cities/')
        self.assertEqual(response.status_code, 400)

        kontinent = Continent.objects.first()

        print ("Testiram pristup cities stranici sa datim id-em:")
        response = self.client.get(f'/cities/?id={kontinent.pk}')
        self.assertEqual(response.status_code, 200)

        print ("Testiram pristup city stranici:")
        response = self.client.get('/city/')
        self.assertEqual(response.status_code, 400)

        grad = City.objects.first()

        print ("Testiram pristup city stranici:")
        response = self.client.get(f'/city/?id={grad.pk}')
        self.assertEqual(response.status_code, 200)

