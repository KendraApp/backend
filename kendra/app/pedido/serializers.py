from rest_framework import serializers
from .models import Pedidos, DetallePedidos
from ..preparacion.serializers import ProductosSerializer
from ..personas.serializers import PersonasSerializer


class PedidosSerializer(serializers.ModelSerializer):
   # asignado_a = serializers.IntegerField(required=False)

    class Meta:
        model = Pedidos
        fields = ('__all__')


class PedidosListSerializer(serializers.ModelSerializer):
    asignado_a = PersonasSerializer()
    producto = ProductosSerializer()

    class Meta:
        model = Pedidos
        fields = ('__all__')


class DetallePedidosSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetallePedidos
        fields = ('__all__')


class PedidoDetalleSerializer(serializers.ModelSerializer):

    pedido = PedidosSerializer()

    class Meta:
        model = DetallePedidos
        fields = ('__all__')


class UpdatePedidosSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=False)
    facturado = serializers.BooleanField(required=False)
    entrega_cocina = serializers.BooleanField(required=False)
    entrega_cliente = serializers.BooleanField(required=False)
    hora_inicio = serializers.TimeField(required=False)
    hora_final = serializers.TimeField(required=False)
    hora_entrega = serializers.TimeField(required=False)

    class Meta:
        model = Pedidos
        fields = ([
            'estado',
            'entrega_cocina',
            'hora_inicio',
            'hora_final',
            'entrega_cliente',
            'hora_entrega',
            'facturado',
        ])
