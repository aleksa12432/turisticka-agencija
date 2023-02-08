from django.db import models

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
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

