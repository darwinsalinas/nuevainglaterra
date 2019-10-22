from django.contrib import admin
from .models import Vendedor, Cliente

admin.site.register([
    Vendedor,
    Cliente,
])
