from django.contrib import admin
from .models import Articulo, Kardex, TipoMovimiento

admin.site.register([
    Articulo,
    Kardex,
    TipoMovimiento
])
