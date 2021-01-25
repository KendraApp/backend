from django.contrib import admin
from .models import *


@admin.register(Promociones)
class PromocionesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('codigo',  'nombre',  'porcentaje',
                    'estado', 'created', 'modified')


@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'gramos',
                    'cantidad_gramos', 'facturable', 'promocion', 'adicion', 'timeout')


@admin.register(InsumosProducto)
class InsumosProductodmin(admin.ModelAdmin):
    list_display = ('producto', 'insumo', 'gramos', 'obligatorio')


admin.site.register(Categoria)
admin.site.register(Proveedor)
