from django.contrib import admin
from .models import Marca, Modelo, Color, UnidadMedida, Presentacion, TipoArticulo, OrigenVenta, TipoFactura

admin.site.register([
    Marca,
    Modelo,
    Color,
    UnidadMedida,
    Presentacion,
    TipoArticulo,
    OrigenVenta,
    TipoFactura
])
