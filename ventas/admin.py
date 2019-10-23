from django.contrib import admin
from .models import Vendedor, Cliente, Venta, DetalleVenta

admin.site.register([
    Vendedor,
    Cliente,
    Venta,
    DetalleVenta
])
