from django.contrib import admin
from .models import Proveedor, Compra, DetalleCompra

admin.site.register([
    Proveedor
])


class DetallesCompraInline(admin.TabularInline):
    model = DetalleCompra


class CompraAdmin(admin.ModelAdmin):
    inlines = [DetallesCompraInline]
    search_fields = [
        'detalles_compra__articulo__nombre'
    ]
    list_filter = ('fecha', 'proveedor__nombre')


class DetalleComrpaAdmin(admin.ModelAdmin):
    search_fields = [
        'articulo__nombre'
    ]
    list_filter = ('compra__fecha', 'compra__proveedor__nombre', 'cantidad')


admin.site.register(Compra, CompraAdmin)
admin.site.register(DetalleCompra, DetalleComrpaAdmin)
