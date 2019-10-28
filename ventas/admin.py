from django.contrib import admin
from .models import Vendedor, Cliente, Venta, DetalleVenta

admin.site.register([
    Vendedor,
    Cliente
])


class DetallesVentaInline(admin.TabularInline):
    model = DetalleVenta


class VentaAdmin(admin.ModelAdmin):
    inlines = [DetallesVentaInline]
    list_filter = ('fecha', 'vendedor__nombres', 'cliente__nombres', 'detalles_venta__articulo__nombre')


admin.site.register(Venta, VentaAdmin)
