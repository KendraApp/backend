from django.contrib import admin
from .models import Facturas


@admin.register(Facturas)
class FacturasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('n_factura',  'personas',  'fecha',
                    'guardado', 'valor', 'descuento', 'created', 'modified')
