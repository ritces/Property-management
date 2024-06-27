from django.db import models


# Create your models here.
class Propiedad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    direccion = models.CharField()
    codigo_postal = models.PositiveIntegerField(blank=True)
    superficie = models.PositiveIntegerField()
    ciudad = models.CharField(max_length=100)
    tipos_opciones = [
        ("CASA", "Casa"),
        ("APTO", "Apartamento"),
        ("OFICINA", "Oficina"),
        ("OTRO", "OTRO"),
    ]
    type = models.CharField(max_length=10, choices=tipos_opciones)
