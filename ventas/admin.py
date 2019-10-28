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
    search_fields = [
        'cliente__nombres'
    ]
    list_filter = ('fecha', 'tipo', 'vendedor__nombres', 'detalles_venta__articulo__nombre')


admin.site.register(Venta, VentaAdmin)
