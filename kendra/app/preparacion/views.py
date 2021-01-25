from django.shortcuts import render

from .models import Productos, InsumosProducto

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from django_filters.rest_framework import (
    DjangoFilterBackend,
)

from .serializers import (
    ProductosSerializer,
    DetalleProductoSerializer,
    InsumosProductoSerializer,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)


class ListProductos(ListAPIView):
    serializer_class = ProductosSerializer
    # queryset = Productos.objects.all()

    def get_queryset(self):
        return Productos.objects.filter(
            facturable=True
        )


class ListProductosAdicion(ListAPIView):
    serializer_class = ProductosSerializer

    def get_queryset(self):
        return Productos.objects.filter(
            adicion=True
        )


class DetalleProductos(ListAPIView):
    serializer_class = DetalleProductoSerializer

    def get_queryset(self):
        producto = self.kwargs['producto']
        return Productos.objects.filter(
            id=producto
        )[0:1]


class InsumosProductosList(ListAPIView):
    serializer_class = InsumosProductoSerializer
    queryset = InsumosProducto.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')
