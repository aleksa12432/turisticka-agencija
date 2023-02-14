from django.contrib.auth.models import User
from django.test import Client, TestCase
from tripify.models import Aranzman, Rezervacija, Profile

class GenerationAndLoginTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.email = 'testuser@example.com'
        self.first_name='first_name'
        self.last_name='last_name'
        self.password = 'secretpassword'
        self.phone_number='+381012345678'
    
    def test_0_register(self):
        print ("Testiram registracionu formu:")
        response = self.client.post('/register/', {
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password1': self.password,
            'password2': self.password,
            'phone_number': self.phone_number
        })
        self.assertEqual(response.status_code, 302)
        user = User.objects.filter(username=self.username)
        self.assertTrue(user.exists())
        self.client.logout()
        user.first().delete()

    def test_1_login_book(self):
        print("Testiram login formu:")

        user = User.objects.create_user(username=self.username, password=self.password, email=self.email, first_name=self.first_name, last_name=self.last_name)

        profil = Profile.objects.create(
            user=user,
            phone_number=self.phone_number
        )

        response = self.client.post('/login/', {
            'username': self.username,
            'password': self.password,
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

        print ("Testiram rezervisanje aranzmana:")
        aranzman= Aranzman.objects.filter(rezervisan=False).first()
        self.client.login(username=self.username, password=self.password)

        print(f'/book/?id={aranzman.pk}, {aranzman.naziv}, {aranzman.rezervisan}')

        response = self.client.post(f'/book/?id={aranzman.pk}', {
            'comment': "test_komentar",
            'payment_method': "1",
            'number_of_adults': "2",
            'number_of_children': "2",
        })

        self.assertEqual(response.status_code, 302)
        rezervacija = Rezervacija.objects.filter(aranzman=aranzman)

        self.assertTrue(rezervacija.exists())

        print("Testiram uklanjanje rezervacije:")

        response = self.client.get(f'/reservations/?cancel=&id={rezervacija.first().pk}')

        self.assertEqual(response.status_code, 200)
    
        rezervacija = Rezervacija.objects.filter(aranzman=aranzman)

        self.assertFalse(rezervacija.exists())


