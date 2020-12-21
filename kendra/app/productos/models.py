from model_utils.models import TimeStampedModel
from django.db import models
from ..insumos.models import Insumos


class Categoria(TimeStampedModel):
    nombre = models.CharField('Categoria', max_length=50)

    def __str__(self):
        return self.nombre


class Clasificacion(TimeStampedModel):
    nombre = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return self.nombre


class Proveedor(TimeStampedModel):
    nombre = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return self.nombre


class Productos(TimeStampedModel):
    nombre = models.CharField('Nombre', max_length=50)
    precio = models.IntegerField('precio', blank=True)
    cantidad = models.IntegerField('cantidad', blank=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='Categoria_productos'
    )
    clasificacion = models.ForeignKey(
        Clasificacion,
        on_delete=models.CASCADE,
        related_name='Clasificacion_producto'
    )
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        related_name='Proveedor_de_producto'
    )
    insumos = models.ManyToManyField(
        Insumos,
        blank=True,
        related_name="Insumos_producto"
    )

    def __str__(self):
        return str(self.nombre) + " " + str(self.clasificacion)
