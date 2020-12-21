from model_utils.models import TimeStampedModel
from django.db import models
from ..productos.models import Productos


class Pedidos(TimeStampedModel):
    producto = models.ForeignKey(
        Productos,
        on_delete=models.CASCADE
    )
    fecha = models.DateField('Fecha')

    def __str__(self):
        return str(self.producto) + " " + str(self.fecha)
