from rest_framework import serializers
from .models import (
    Produccion,
    ProduccionProducto,
    Sabores,
    DetalleProducion,
    BasesProduccion,
    DetalleBase,
    ConsumoProduccion,
    Categoria,
)
from ..insumos.serializers import InsumosSerializer


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')


class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produccion
        fields = ('__all__')


class BasesProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasesProduccion
        fields = ('__all__')


class SaboresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sabores
        fields = ('__all__')


class ProduccionProductoSerializer(serializers.ModelSerializer):
    sabor = SaboresSerializer()
    categoria = CategoriaSerializer()

    class Meta:
        model = ProduccionProducto
        fields = ('__all__')


class UpdateGramosroduccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProduccionProducto
        fields = (['gramos'])


class DetalleProduccionSerializer(serializers.ModelSerializer):
    # producto_rela = serializers.IntegerField(required=False)
    # insumos = serializers.IntegerField(required=False)

    class Meta:
        model = DetalleProducion
        fields = ('__all__')


class DetalleBaseSerializer(serializers.ModelSerializer):
    insumo = InsumosSerializer()
    producto = ProduccionProductoSerializer()

    class Meta:
        model = DetalleBase
        fields = ('__all__')


class ConsumoProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumoProduccion
        fields = ('__all__')
