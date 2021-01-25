from django.contrib import admin
from .models import *


# admin.site.register(Pedidos)
@admin.register(Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('producto', 'asignado_a', 'estado',
                    'cliente_name', 'valor', 'created', 'modified')


class DetallePedidosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')


@admin.register(CoordinacionCocina)
class CoordinacionCocinaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('persona', 'fecha', 'created', 'modified')


admin.site.register(DetallePedidos, DetallePedidosAdmin)
