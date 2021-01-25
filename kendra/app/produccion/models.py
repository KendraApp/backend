from model_utils.models import TimeStampedModel
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from ..insumos.models import Insumos


class Categoria(TimeStampedModel):
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categoria"

    nombre = models.CharField('Nombre ', max_length=100)

    def __str__(self):
        return self.nombre


class Sabores(TimeStampedModel):

    class Meta:
        verbose_name = "Sabores"
        verbose_name_plural = "Sabores"

    nombre = models.CharField('Nombre del sabor', max_length=100)

    def __str__(self):
        return self.nombre


class BasesProduccion(TimeStampedModel):

    class Meta:
        verbose_name = "Bases"
        verbose_name_plural = "Bases"

    nombre = models.CharField('Nombre de la base', max_length=100)

    def __str__(self):
        return self.nombre


class ProduccionProducto(TimeStampedModel):

    class Meta:
        verbose_name = "Productos"
        verbose_name_plural = "Productos"

    nombre = models.CharField('Nombre', blank=True, max_length=100)
    cantidad = models.IntegerField('Total cantidad', blank=True, default=0)
    gramos = models.IntegerField('Total gramos', blank=True, default=0)
    sabor = models.ForeignKey(
        Sabores,
        blank=True,
        related_name="Sabor_produccion",
        on_delete=models.CASCADE,
        null=True
    )
    categoria = models.ForeignKey(
        Categoria,
        related_name="Categoria_producto",
        on_delete=models.SET_NULL,
        null=True
    )
    base = models.ForeignKey(
        BasesProduccion,
        verbose_name='base',
        related_name="base_producto",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.nombre)+" "+str(self.gramos) + " "+str(self.sabor)


class DetalleBase(TimeStampedModel):

    class Meta:
        verbose_name = "Detalle Base",
        verbose_name_plural = "Detalle Base"

    base = models.ForeignKey(
        BasesProduccion,
        on_delete=models.SET_NULL,
        related_name='base',
        null=True
    )
    insumo = models.ForeignKey(
        Insumos,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='insumo'
    )
    producto = models.ForeignKey(
        ProduccionProducto,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='producto_base'
    )
    porcentaje = models.IntegerField('Porcentaje', default=0)
    isprod = models.BooleanField('¿Es un producto?', default=False)

    def __str__(self):
        return str(self.base)+" "+str(self.insumo)+" "+str(self.porcentaje)


class Produccion(TimeStampedModel):

    class Meta:
        verbose_name = "Producción"
        verbose_name_plural = "Producción"

    producto = models.ForeignKey(
        ProduccionProducto,
        related_name="producto_produccion",
        on_delete=models.CASCADE
    )
    cantidad = models.IntegerField('Cantidad producida', default=0)
    gramos = models.IntegerField('Gramos unitario', default=0)
    total_gramos = models.IntegerField('Total producido', default=0)
    fecha = models.DateField('Fecha', auto_now_add=True)

    def __str__(self):
        return str(self.producto)


class ConsumoProduccion(TimeStampedModel):
    class Meta:
        verbose_name = "Consumo Produccion"
        verbose_name_plural = "Consumo Produccion"

    producto = models.ForeignKey(
        ProduccionProducto,
        related_name="producto_consumo",
        on_delete=models.CASCADE
    )
    gramos = models.IntegerField('Gramos')
    fecha = models.DateField('Fecha', auto_now_add=True)

    def __str__(self):
        return str(self.producto)+" "+str(self.gramos)


class DetalleProducion(TimeStampedModel):

    class Meta:
        verbose_name = "Detalle Produccion"
        verbose_name_plural = "Detalle Produccion"

    producto = models.ForeignKey(
        ProduccionProducto,
        related_name="producto",
        on_delete=models.CASCADE
    )
    insumos = models.ForeignKey(
        Insumos,
        blank=True,
        null=True,
        related_name='Insumos',
        on_delete=models.CASCADE,
    )
    producto_rela = models.ForeignKey(
        ProduccionProducto,
        related_name="producto_to_producto",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    gramos = models.IntegerField('Gramos utilizados', blank=True)
    fecha = models.DateField('Fecha', blank=True, auto_now_add=True)

    def __str__(self):
        return str(self.producto) + " " + str(self.fecha) + " " + str(self.gramos)


# @receiver(post_save, sender=DetalleProducion)
# def set_gramos(sender, instance, created, **kwargs):

#     if created:
#         # instance.producto.gramos += instance.gramos
#         # instance.producto.save()

#         # Descontamos los gramos de los insumos utilizados
#         instance.insumos.gramos -= instance.gramos
#         instance.insumos.save()


# class UnidadMedidad(TimeStampedModel):

#     class Meta:
#         verbose_name = "Produccion Helados"
#         verbose_name_plural = "Produccion Helados"

#     nombre = models.CharField('Unidad de medida', max_length=100)

#     def __str__(self):
#         return self.nombre
