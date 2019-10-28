from django.contrib import admin
from .models import OrigenPedido, Pedido, DetallePedido

admin.site.register([
    OrigenPedido,
])


class DetallesPedidoInline(admin.TabularInline):
    model = DetallePedido


class PedidoAdmin(admin.ModelAdmin):
    inlines = [DetallesPedidoInline]
    list_filter = ('fecha', 'vendedor__nombres', 'cliente__nombres', 'origen__nombre')


admin.site.register(Pedido, PedidoAdmin)
