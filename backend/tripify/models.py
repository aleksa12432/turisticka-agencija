from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Continent(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tripify/static/')

    def __str__(self):
        return self.name

class Tipovi_smestaja(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Tip_sobe(models.Model):
    name = models.CharField(max_length=20)
    broj_ljudi = models.IntegerField()

    def __str__(self):
        return self.name
    
class Tip_prevoza(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Smestaj(models.Model):
    name = models.CharField(max_length=100)
    kategorija = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    internet = models.BooleanField()
    tv = models.BooleanField()
    klima = models.BooleanField()
    sobni_frizider = models.BooleanField()
    cena_prevoza = models.IntegerField(
        validators=[
            MaxValueValidator(3000),
            MinValueValidator(100)
        ]
    )
    grad = models.ForeignKey(City, on_delete=models.CASCADE)
    tip_smestaja = models.ForeignKey(Tipovi_smestaja, on_delete=models.CASCADE)
    tip_sobe = models.ForeignKey(Tip_sobe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Smestaj_slika(models.Model):
    img = models.ImageField(upload_to='tripify/static')
    smestaj = models.ForeignKey(Smestaj, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.smestaj.name} - {self.img.url}"
    

class Aranzman(models.Model):
    naziv = models.CharField(max_length=255, unique=True)
    opis = models.CharField(max_length=512)
    prevoz = models.ForeignKey(Tip_prevoza, on_delete=models.CASCADE)
    smestaj = models.ForeignKey(Tipovi_smestaja, on_delete=models.CASCADE)
    cena = models.IntegerField(
        validators=[
            MaxValueValidator(3000),
            MinValueValidator(500)
        ]
    )
    polazak = models.DateTimeField()
    duzina = models.IntegerField( # duzina u danima
        validators=[ # 1 do 2 nedelje
            MaxValueValidator(14),
            MinValueValidator(7)
        ]
    )
    rezervisan = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.naziv

class Termin(models.Model):
    aranzman = models.ForeignKey(Aranzman, on_delete=models.CASCADE)
    smestaj = models.ForeignKey(Smestaj, on_delete=models.CASCADE)
    vreme_stizanja = models.DateTimeField()

    def __str__(self):
        return f"{self.aranzman.naziv} - {self.smestaj.name}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.user.username
    

class Rezervacija(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    aranzman = models.ForeignKey(Aranzman, on_delete=models.CASCADE)
    broj_odraslih = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    broj_dece = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    NACINI_PLACANJA = [
        (0, 'card'),
        (1, 'cash')
    ]
    nacin_placanja = models.IntegerField(
        choices=NACINI_PLACANJA
    )
    komentar = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.user.first_name} - {self.aranzman.naziv}"
    