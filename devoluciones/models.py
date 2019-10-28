from django.db import models
from ventas.models import Cliente, Vendedor
from inventario.models import Articulo


class Devolucion(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.fecha, self.cliente.nombres)

    class Meta:
        verbose_name = 'Devolución'
        verbose_name_plural = 'Devoluciones'


class DetalleDevolucion(models.Model):
    devolucion = models.ForeignKey(Devolucion, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)
    cantidad = models.FloatField()
    precio_devolucion = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.cantidad, self.articulo.nombre)

    class Meta:
        verbose_name = 'Detalle de devolución'
        verbose_name_plural = 'Detalles de devoluciones'
