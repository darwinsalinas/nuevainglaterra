from django.db import models
from catalogos.models import Genero, Comunidad, EstadoCivil
from inventario.models import Articulo, Kardex
from django.db.models.signals import post_save
from django.dispatch import receiver


class OrigenPedido(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Origen de venta'
        verbose_name_plural = 'Orígenes de ventas'


class TipoVenta(models.Model):
    nombre = models.CharField(max_length=60)
    descuento = models.FloatField(default=0)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Tipo de venta'
        verbose_name_plural = 'Tipos de ventas'


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


class Pedido(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.PROTECT)
    origen = models.ForeignKey(OrigenPedido, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.fecha)

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


class Venta(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoVenta, on_delete=models.PROTECT)  # Al por mayor y al menudeo

    def __str__(self):
        return "{}".format(self.fecha)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)
    cantidad = models.FloatField()
    precio_venta = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.cantidad, self.articulo.nombre)

    class Meta:
        verbose_name = 'Detalle de venta'
        verbose_name_plural = 'Detalles de ventas'


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


@receiver(post_save, sender=DetalleVenta)
def actualizar_inventario(sender, instance, **kwargs):
    venta_id = instance.venta.id
    articulo_id = instance.articulo.id
    fecha_venta = instance.venta.fecha

    kardex = Kardex()
    kardex.fecha = fecha_venta
    kardex.referencia = "Venta No {}".format(venta_id)
    kardex.articulo_id = articulo_id
    kardex.tipo_movimiento = 2
    kardex.cantidad = instance.cantidad
    kardex.valor_unitario = instance.precio_venta
    kardex.save()
