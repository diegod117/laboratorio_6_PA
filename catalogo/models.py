from django.db import models

# Create your models here.


class Tienda(models.Model):
    nombre = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=100)
    sitio_web = models.URLField()

    def __str__(self):
        return self.nombre

