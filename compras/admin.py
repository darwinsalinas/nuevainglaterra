from django.contrib import admin
from .models import Proveedor, Compra, DetalleCompra

admin.site.register([
    Proveedor,
    Compra,
    DetalleCompra,
])
