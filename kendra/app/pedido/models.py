from model_utils.models import TimeStampedModel
from django.db import models
from ..preparacion.models import Productos
from ..personas.models import Personas
from ..insumos.models import Insumos
from ..produccion.models import ProduccionProducto


class CoordinacionCocina(TimeStampedModel):
    persona = models.ForeignKey(
        Personas,
        on_delete=models.CASCADE
    )
    fecha = models.DateField('Fecha', auto_now_add=True)

    def __str__(self):
        return str(self.persona)+" "+str(self.fecha)


class Pedidos(TimeStampedModel):
    producto = models.ForeignKey(
        Productos,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    asignado_a = models.ForeignKey(
        Personas,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="asignado_a"
    )
    fecha = models.DateField('Fecha', auto_now_add=True)
    observacion = models.CharField('Observacion', max_length=100, blank=True)
    cantidad = models.IntegerField('Cantidad', default=1, blank=False)
    cancelado = models.BooleanField('Cancelado', default=False)
    estado = models.BooleanField('Estado Cocina', default=False)
    facturado = models.BooleanField('Facturado', default=False)
    entrega_cocina = models.BooleanField('Entrega de Cocina', default=False)
    entrega_cliente = models.BooleanField('Entrega a Cliente', default=False)
    hora_inicio = models.TimeField(
        'Hora de preparación', blank=True, null=True)
    hora_final = models.TimeField('Hora de finalizcion', blank=True, null=True)
    hora_entrega = models.TimeField('Hora de entrega', blank=True, null=True)

    cliente_name = models.CharField('Cliente', max_length=100, blank=True)
    valor = models.BigIntegerField('Valor', blank=True, default=0)
    desc_pedido = models.TextField('Descripción Pedido', blank=True)
    condiciones = models.TextField('Condiciones Pedido', blank=True)

    def __str__(self):
        return str(self.producto) + " " + str(self.fecha) + " " + str(self.observacion)


class DetallePedidos(TimeStampedModel):
    pedido = models.ForeignKey(
        Pedidos,
        on_delete=models.CASCADE,
    )
    insumo = models.ForeignKey(
        Insumos,
        on_delete=models.SET_NULL,
        related_name="insumo_pedido",
        null=True,
        blank=True,
    )
    produccion = models.ForeignKey(
        ProduccionProducto,
        on_delete=models.SET_NULL,
        related_name="produccion_pedido",
        null=True,
        blank=True,
    )
    ingrediente_name = models.CharField(
        'Ingrediente/Asumo/Adicion', max_length=100)
    gramos = models.IntegerField('Gramos utilizados', blank=True, default=0)
    valor = models.BigIntegerField('Valor', blank=True, default=0)

    def __str__(self):
        return str(self.pedido) + " " + str(self.ingrediente_name)
