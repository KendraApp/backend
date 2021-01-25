from django.shortcuts import render
from .models import Pedidos, DetallePedidos
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from django_filters.rest_framework import (
    DjangoFilterBackend,
)

from .serializers import (
    PedidosSerializer,
    DetallePedidosSerializer,
    PedidoDetalleSerializer,
    PedidosListSerializer,
    UpdatePedidosSerializer,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)


class PedidosList(ListAPIView):
    serializer_class = PedidosListSerializer
    queryset = Pedidos.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = [
        'id',
        'estado',
        'entrega_cocina',
        'entrega_cliente',
        'facturado',
    ]
    search_fields = [
        'cliente_name',
    ]
    ordering_fields = (
        'id',
        'estado',
        'hora_incio',
        'hora_final',
        'modified',
        'hora_entrega',
    )


class CreatePedido(CreateAPIView):
    serializer_class = PedidosSerializer
    queryset = Pedidos.objects.all()


class CreateDetalle(CreateAPIView):
    serializer_class = DetallePedidosSerializer
    queryset = DetallePedidos.objects.all()


class DetallePedidoList(ListAPIView):
    serializer_class = PedidoDetalleSerializer

    def get_queryset(self):
        pedido = self.kwargs['pedido']
        return DetallePedidos.objects.filter(
            pedido=pedido
        )


class UpdatePedido(RetrieveUpdateAPIView):
    serializer_class = PedidosSerializer
    queryset = Pedidos.objects.all()
