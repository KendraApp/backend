from model_utils.models import TimeStampedModel
from django.db import models
from ..pedido.models import Pedidos
from ..insumos.models import Insumos


class Operacion(TimeStampedModel):
    pedido = models.ForeignKey(
        Pedidos,
        on_delete=models.CASCADE,
    )
    insumo = models.ForeignKey(
        Insumos,
        on_delete=models.CASCADE
    )
    cantidad = models.IntegerField('Cantidad utilizada')

    def __str__(self):
        return str(self.pedido) + " " + str(self.insumo)
