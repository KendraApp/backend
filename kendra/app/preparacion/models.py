from model_utils.models import TimeStampedModel
from django.db import models
from ..produccion.models import Insumos, ProduccionProducto


class Promociones(TimeStampedModel):
    class Meta:
        verbose_name = "Promociones y Descuentos"
        verbose_name_plural = "Promociones y Descuentos"

    codigo = models.CharField("Código", unique=True, max_length=50)
    nombre = models.CharField('Nombre', blank=True, max_length=100)
    porcentaje = models.IntegerField('Porcentaje', default=0)
    fecha_inicio = models.DateField('Fecha de inicio',  blank=True, null=True)
    fecha_final = models.DateField(
        'Fecha de vencimiento', blank=True, null=True)
    hora_inicio = models.TimeField('Hora de inicio', blank=True, null=True)
    hora_final = models.TimeField('Hora de vencimiento', blank=True, null=True)
    estado = models.BooleanField('Visible', default=False)

    def __str__(self):
        return str(self.codigo)+" "+str(self.nombre)


class Categoria(TimeStampedModel):

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categoria"

    nombre = models.CharField('Categoria', max_length=50)

    def __str__(self):
        return self.nombre


class Proveedor(TimeStampedModel):

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedor"

    nombre = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return self.nombre


class Productos(TimeStampedModel):

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Producto"

    nombre = models.CharField('Nombre', max_length=50)
    precio = models.IntegerField('precio', blank=True, default=0, null=True)
    cantidad = models.IntegerField(
        'cantidad', blank=True, default=0, null=True)
    stock = models.IntegerField('stock', blank=True, default=0, null=True)
    gramos = models.IntegerField(
        'Gramos para Helado/Pulpa', blank=True, default=0, null=True)
    cantidad_gramos = models.IntegerField(
        'Bolas de Helado/Pulpa', blank=True, default=0, null=True)
    timeout = models.IntegerField(
        'Tiempo de espera', blank=True, default=0, null=True)
    photo = models.ImageField(blank=True, upload_to="productos", null=True)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="Categoria_productos"
    )

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        related_name="Proveedor_de_producto"
    )
    promocion = models.ForeignKey(
        Promociones,
        on_delete=models.SET_NULL,
        null=True,
        related_name="Promocion_de_producto",
        blank=True,
    )
    facturable = models.BooleanField('Facturable', default=True)
    adicion = models.BooleanField('Adicion', default=False)

    def __str__(self):
        return str(self.nombre)


class InsumosProducto(TimeStampedModel):
    class Meta:
        verbose_name = "InsumosProducto"
        verbose_name_plural = "InsumosProducto"

    producto = models.ForeignKey(
        Productos,
        on_delete=models.CASCADE,
        related_name="producto_insumo",
    )
    insumo = models.ForeignKey(
        Insumos,
        on_delete=models.CASCADE,
        related_name="insumo_producto",
    )
    gramos = models.IntegerField('Gramos a utilizar', default=0)
    obligatorio = models.BooleanField('Obligatorio', default=False)

    def __str__(self):
        return str(self.producto) + " " + str(self.insumo) + str(self.gramos)
