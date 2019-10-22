from django.db import models
from catalogos.models import Marca, Modelo, UnidadMedida, Presentacion, TipoArticulo


class Articulo(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=20)
    serie = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE)
    tipo_articulo = models.ForeignKey(TipoArticulo, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
