from django.db import models
from ventas.models import Cliente, Vendedor
from inventario.models import Articulo, Kardex
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    devolucion = models.ForeignKey(Devolucion, on_delete=models.CASCADE, related_name='detalles_devolucion')
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)
    cantidad = models.FloatField()
    precio_devolucion = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.cantidad, self.articulo.nombre)

    class Meta:
        verbose_name = 'Detalle de devolución'
        verbose_name_plural = 'Detalles de devoluciones'


@receiver(post_save, sender=DetalleDevolucion)
def actualizar_inventario(sender, instance, **kwargs):
    devolucion_id = instance.devolucion.id
    articulo_id = instance.articulo.id
    fecha_compra = instance.devolucion.fecha

    kardex = Kardex()
    kardex.fecha = fecha_compra
    kardex.referencia = "Devolución No {}".format(devolucion_id)
    kardex.articulo_id = articulo_id
    kardex.tipo_movimiento_id = 3
    kardex.cantidad = instance.cantidad
    kardex.valor_unitario = instance.precio_devolucion
    kardex.save()
