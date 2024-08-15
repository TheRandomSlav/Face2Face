from django.db import models


class Persona(models.Model):
    name = models.CharField(max_length=255)
    embedding = models.BinaryField()

    def __str__(self):
        return self.name
# Create your models here.


class FImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='imag/')
    def __str__(self):
        return self.name