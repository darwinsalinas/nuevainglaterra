from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Marca, Modelo, UnidadMedida, Presentacion, TipoArticulo, Genero, \
    EstadoCivil, Pais, Departamento, Municipio, Comunidad
from ventas.models import TipoVenta

admin.site.register([
    Marca,
    Modelo,
    UnidadMedida,
    Presentacion,
    TipoArticulo,
    Genero,
    EstadoCivil,
    Pais,
    Departamento,
    Municipio,
    Comunidad,
    TipoVenta
])

admin.site.unregister([
    Group, User
])
