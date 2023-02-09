from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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

