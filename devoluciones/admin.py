from django.contrib import admin
from .models import Devolucion, DetalleDevolucion


class DetallesDevolucionInline(admin.TabularInline):
    model = DetalleDevolucion


class DevolucionAdmin(admin.ModelAdmin):
    inlines = [DetallesDevolucionInline]
    search_fields = [
        'detalles_devolucion__articulo__nombre'
    ]
    list_filter = ('fecha', 'cliente__nombres')


class DetalleDevolucionAdmin(admin.ModelAdmin):
    search_fields = [
        'articulo__nombre'
    ]
    list_filter = ('devolucion__fecha', 'devolucion__cliente__nombres', 'cantidad')


admin.site.register(Devolucion, DevolucionAdmin)
admin.site.register(DetalleDevolucion, DetalleDevolucionAdmin)
