from django.contrib.auth.models import User
from django.test import Client, TestCase

class GenerationAndLoginTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.email = 'testuser@example.com'
        self.first_name='first_name'
        self.last_name='last_name'
        self.password = 'secretpassword'
        self.phone_number='+381012345678'
    
    def test_register(self):
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
        self.assertTrue(User.objects.filter(username=self.username).exists())

    def test_login(self):
        print("Testiram login formu:")
        User.objects.create_user(username=self.username, password=self.password)
        response = self.client.post('/login/', {
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)