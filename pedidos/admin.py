from django.contrib import admin
from .models import OrigenPedido, Pedido, DetallePedido

admin.site.register([
    OrigenPedido,
])


class DetallesPedidoInline(admin.TabularInline):
    model = DetallePedido


class PedidoAdmin(admin.ModelAdmin):
    inlines = [DetallesPedidoInline]
    search_fields = [
        'cliente__nombres'
    ]
    list_filter = ('fecha', 'vendedor__nombres', 'origen__nombre')


admin.site.register(Pedido, PedidoAdmin)
