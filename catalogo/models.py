from django.db import models

# Create your models here.


# ===== Producto (Diego) =====
class Producto(models.Model):
    """Producto de Pokémon TCG (reemplaza la lista en memoria del Laboratorio 6)."""

    TIPOS = [
        ('sobre', 'Sobre'),
        ('caja', 'Caja'),
        ('carta', 'Carta'),
    ]

    nombre = models.CharField(max_length=150)
    expansion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)

    def __str__(self):
        return self.nombre
# ===== Fin Producto (Diego) =====
