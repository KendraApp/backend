from model_utils.models import TimeStampedModel
from django.db import models
from ..insumos.models import Insumos


class Compras(TimeStampedModel):
    insumo = models.ForeignKey(
        Insumos,
        on_delete=models.CASCADE,
        related_name="Compra_insumos"
    )
    cantidad = models.IntegerField('Cantidad')
    fecha = models.DateField('Fecha de compra')
    precio = models.IntegerField('Precio')

    def __str__(self):
        return str(self.insumo) + " " + str(self.precio) + " " + str(self.fecha) + " " + str(self.cantidad)
