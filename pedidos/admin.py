from django.contrib import admin
from .models import OrigenPedido, Pedido, DetallePedido

admin.site.register([
    OrigenPedido,
    Pedido,
    DetallePedido
])
