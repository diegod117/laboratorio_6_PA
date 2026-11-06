from django.db import models

# Create your models here.


# ===== Oferta (Johann) =====
class Oferta(models.Model):
    producto = models.CharField(max_length=100)
    tienda = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.producto} - {self.tienda}"
# ===== Fin Oferta (Johann) =====


class Tienda(models.Model):
    nombre = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=100)
    sitio_web = models.URLField()

    def __str__(self):
        return self.nombre
