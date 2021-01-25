from django.contrib import admin
from .models import *


@admin.register(Unidad_Medida)
class Unidad_MedidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'valor')


@admin.register(Insumos)
class InsumosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rendimiento', 'cantidad',
                    'gramos', 'unidad_medida')


@admin.register(ConsumoInsumo)
class ConsumoInsumoAdmin(admin.ModelAdmin):
    list_display = ('insumo', 'gramos', 'fecha')


# @admin.register(StockInsumo)
# class StockInsumoAdmin(admin.ModelAdmin):
#     list_display = ('insumo', 'cantidad', 'gramos')


@admin.register(Compras)
class ComprasAdmin(admin.ModelAdmin):
    list_display = ('insumo', 'unidad_medida', 'cantidad', 'gramos_unidad',
                    'gramos', 'precio_unidad', 'precio', 'fecha')
