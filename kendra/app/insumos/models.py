from model_utils.models import TimeStampedModel
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Unidad_Medida(TimeStampedModel):
    class Meta:
        verbose_name = "Unidad de medida"
        verbose_name_plural = "Unidad de medida"

    nombre = models.CharField('Nombre de unidad', max_length=100)
    valor = models.FloatField('¿Valor en gramos?', default=0)

    def __str__(self):
        return str(self.nombre)+" "+str(self.valor)


class Insumos(TimeStampedModel):

    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumo"

    unidad_medida = models.ForeignKey(
        Unidad_Medida,
        verbose_name='unidad de medida',
        related_name='unidad_medida',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    nombre = models.CharField('Nombre', max_length=50)
    rendimiento = models.PositiveSmallIntegerField(
        'Rendimiento(Porc)', default=100, null=True, blank=True)
    cantidad = models.IntegerField('Cantidad', blank=True, default=0)
    gramos = models.IntegerField(
        'Gramos últiles', default=0, null=True, blank=True)

    # restante = models.IntegerField('Restante', blank=True, default=0)
    # gramos = models.IntegerField('Gramos totales', blank=True, default=0)
    # gramos_util = models.IntegerField(
    #     'Gramos últiles', default=0, null=True, blank=True)

    def __str__(self):
        return str(self.nombre)


class Compras(TimeStampedModel):
    insumo = models.ForeignKey(
        Insumos,
        on_delete=models.CASCADE,
        related_name="Compra_insumos"
    )
    unidad_medida = models.ForeignKey(
        Unidad_Medida,
        on_delete=models.SET_NULL,
        related_name="unidad",
        blank=True,
        null=True,
    )
    fecha = models.DateField('Fecha de compra')
    cantidad = models.IntegerField('Cantidad', blank=True, default=0)
    gramos_unidad = models.IntegerField(
        'Gramos x Unidad', blank=True, default=0)
    precio_unidad = models.IntegerField(
        'Precio x  Unidad', blank=True, default=0)
    gramos_total = models.IntegerField('Gramos Total', blank=True, default=0)
    gramos = models.IntegerField('Gramos Útiles', blank=True, default=0)
    precio = models.IntegerField('Precio Total', blank=True, default=0)

    def __str__(self):
        return str(self.insumo) + " " + str(self.precio) + " " + str(self.fecha) + " " + str(self.cantidad)


class ConsumoInsumo(TimeStampedModel):
    insumo = models.ForeignKey(
        Insumos,
        on_delete=models.CASCADE,
        related_name="Consumo_insumos"
    )
    gramos = models.IntegerField('Gramos')
    fecha = models.DateField('Fecha', auto_now_add=True)

    def __str__(self):
        return str(self.insumo) + " "+str(self.gramos) + " "+str(self.fecha)


@receiver(post_save, sender=Compras)
def set_gramos(sender, instance, created, **kwargs):

    if created:
        instance.insumo.gramos += instance.gramos
        instance.insumo.cantidad += instance.cantidad
        # instance.insumo.gramos_util = (
        # instance.insumo.gramos*instance.insumo.rendimiento)/100
        instance.insumo.save()
