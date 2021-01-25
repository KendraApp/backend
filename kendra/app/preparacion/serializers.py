from rest_framework import serializers
from .models import Productos, Categoria, InsumosProducto
from ..insumos.serializers import InsumosSerializer


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('__all__')


class ProductosSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    # insumos = InsumosSerializer(many=True)

    class Meta:
        model = Productos
        fields = ('__all__')


class DetalleProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    # insumos = InsumosSerializer(many=True)

    class Meta:
        model = Productos
        fields = ([
            'id',
            'categoria',
            'precio',
            'photo',
            'nombre',
            'gramos',
            'cantidad_gramos',
        ])


class InsumosProductoSerializer(serializers.ModelSerializer):
    insumo = InsumosSerializer()

    class Meta:
        model = InsumosProducto
        fields = ('__all__')
