from django.contrib import admin
from .models import Articulo, Kardex, TipoMovimiento

admin.site.register([
    Kardex,
    TipoMovimiento
])


class ArticuloAdmin(admin.ModelAdmin):
    search_fields = [
        'nombre',
        'codigo',
        'serie'
    ]
    list_filter = (
        'marca__nombre',
        'modelo__nombre',
        'unidad_medida__nombre',
        'presentacion__nombre',
        'tipo_articulo__nombre'
    )


admin.site.register(Articulo, ArticuloAdmin)
