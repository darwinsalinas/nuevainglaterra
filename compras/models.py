from django.db import models
from catalogos.models import Comunidad
from inventario.models import Articulo, Kardex
from django.db.models.signals import post_save
from django.dispatch import receiver


class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=250)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class Compra(models.Model):
    fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.fecha)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    precio_compra = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.cantidad, self.articulo.nombre)

    class Meta:
        verbose_name = 'Detalle de compra'
        verbose_name_plural = 'Detalles de compras'


@receiver(post_save, sender=DetalleCompra)
def actualizar_inventario(sender, instance, **kwargs):
    compra_id = instance.compra.id
    articulo_id = instance.articulo.id
    fecha_compra = instance.compra.fecha

    kardex = Kardex()
    kardex.fecha = fecha_compra
    kardex.referencia = compra_id
    kardex.articulo_id = articulo_id
    kardex.tipo_movimiento = 1
    kardex.cantidad = instance.cantidad
    kardex.valor_unitario = instance.precio_compra
    kardex.save()
