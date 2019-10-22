from django.db import models
from catalogos.models import Genero, Comunidad, EstadoCivil


class Vendedor(models.Model):
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=250)

    def __str__(self):
        return "{} {}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'


class Cliente(models.Model):
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=250)

    def __str__(self):
        return "{} {}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
