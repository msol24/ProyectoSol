from django.db import models

# Create your models here.
class We(models.Model):
    publicacion = models.DateField()
    suscriptor = models.CharField(max_length=40)
    critica = models.CharField(max_length=200)

class TheCar(models.Model):
    publicacion = models.DateField()
    suscriptor = models.CharField(max_length=40)
    critica = models.CharField(max_length=200)

class WOTP(models.Model):
    publicacion = models.DateField()
    suscriptor = models.CharField(max_length=40)
    critica = models.CharField(max_length=200)

class RHCP(models.Model):
    publicacion = models.DateField()
    suscriptor = models.CharField(max_length=40)
    critica = models.CharField(max_length=200)

class Phoenix(models.Model):
    publicacion = models.DateField()
    suscriptor = models.CharField(max_length=40)
    critica = models.CharField(max_length=200)

# models de funcionalidad

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    acepta_mails = models.BooleanField()

class Posteo(models.Model):
    id_post = models.IntegerField()
    nombre = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    descripcion = models.CharField(max_length=100)