from django.db import models
from inventario.models import Articulo
from ventas.models import Cliente, Vendedor


class OrigenPedido(models.Model):
    nombre = models.CharField(max_length=60, verbose_name='Origen del pedido')

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Origen de pedido'
        verbose_name_plural = 'Orígenes de pedidos'


class Pedido(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.PROTECT)
    origen = models.ForeignKey(OrigenPedido, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.fecha, self.cliente.nombres)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)
    cantidad = models.FloatField()
    precio_venta = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.cantidad, self.articulo.nombre)

    class Meta:
        verbose_name = 'Detalle de pedido'
        verbose_name_plural = 'Detalles de pedidos'
