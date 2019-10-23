from django.contrib import admin
from .models import Articulo, Kardex

admin.site.register([
    Articulo,
    Kardex
])
