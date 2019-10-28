from django.contrib import admin
from .models import Proveedor, Compra, DetalleCompra

admin.site.register([
    Proveedor
])


class DetallesCompraInline(admin.TabularInline):
    model = DetalleCompra


class CompraAdmin(admin.ModelAdmin):
    inlines = [DetallesCompraInline]
    list_filter = ('fecha', 'proveedor__nombre', 'detalles_compra__articulo__nombre')


admin.site.register(Compra, CompraAdmin)