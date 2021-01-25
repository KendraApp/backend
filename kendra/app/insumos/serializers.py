from rest_framework import serializers
from .models import Insumos, Compras, Unidad_Medida, ConsumoInsumo


class UnidadMedidaSerializer(serializers.ModelSerializer):
    # persona = PersonasSerializer()

    class Meta:
        model = Unidad_Medida
        fields = ('__all__')


class InsumosSerializer(serializers.ModelSerializer):
    # persona = PersonasSerializer()

    class Meta:
        model = Insumos
        fields = ('__all__')


class ShopInsumosSerializer(serializers.ModelSerializer):
    insumo = InsumosSerializer()

    class Meta:
        model = Compras
        fields = ('__all__')


class AddShopInsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = ('__all__')


class UpdateGramosInsumosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Insumos
        fields = (['gramos'])


class ConsumoInsumoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsumoInsumo
        fields = ('__all__')
