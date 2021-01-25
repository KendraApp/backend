from django.db import models
from model_utils.models import TimeStampedModel
from ..pedido.models import Pedidos
from ..personas.models import Personas


class Facturas(TimeStampedModel):

    class Meta:
        verbose_name = "Facturas"
        verbose_name_plural = "Facturas"

    n_factura = models.CharField(
        'Número de factura', max_length=256, blank=True, null=True)
    pedidos = models.ManyToManyField(
        Pedidos,
        related_name="Pedidos"
    )
    personas = models.ForeignKey(
        Personas,
        on_delete=models.CASCADE,
        related_name='Persona_factura'
    )
    descuento = models.CharField(
        'Descuento aplicado', blank=True, max_length=100)
    guardado = models.BooleanField('Guardado', default=False)
    fecha = models.DateField('Fecha', auto_now_add=True)
    valor = models.BigIntegerField('Valor', default=0)

    def __str__(self):
        return str(self.n_factura) + " " + str(self.personas) + " " + str(self.fecha)
