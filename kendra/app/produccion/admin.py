from django.contrib import admin
from .models import *

# from .forms import (
#     InsumosAdminForm
# # )


# class InsumosInlineAdmin(admin.TabularInline):
#     form: InsumosAdminForm
#     model = Insumos


@admin.register(BasesProduccion)
class BaseAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(DetalleBase)
class DetalleBaseAdmin(admin.ModelAdmin):
    list_display = ('base', 'insumo', 'producto', 'porcentaje',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(ProduccionProducto)
class ProduccionProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sabor', 'gramos', 'categoria', 'base')


@admin.register(Sabores)
class SaboresAdmin(admin.ModelAdmin):
    pass


@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'gramos', 'total_gramos', 'fecha')


@admin.register(ConsumoProduccion)
class ConsumoProduccionAdmin(admin.ModelAdmin):
    list_display = ('producto', 'gramos', 'fecha')


@admin.register(DetalleProducion)
class DetalleProduccionAdmin(admin.ModelAdmin):
    list_display = ('producto', 'insumos', 'producto_rela', 'gramos', 'fecha')
