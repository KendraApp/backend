from django.shortcuts import render

from .models import (
    Produccion,
    ProduccionProducto,
    Sabores,
    DetalleProducion,
    BasesProduccion,
    DetalleBase,
    ConsumoProduccion,
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from django_filters.rest_framework import (
    DjangoFilterBackend,
    FilterSet,
    filters
)

from .serializers import (
    ProduccionProductoSerializer,
    SaboresSerializer,
    UpdateGramosroduccionSerializer,
    DetalleProduccionSerializer,
    BasesProduccionSerializer,
    DetalleBaseSerializer,
    ProduccionSerializer,
    ConsumoProduccionSerializer,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)


class Filtered(FilterSet):
    negated_producto__not = filters.NumberFilter(
        field_name='id', exclude=True)

    class Meta:
        model = ProduccionProducto
        fields = ('__all__')


class ListProduccion(ListAPIView):
    serializer_class = ProduccionProductoSerializer
    queryset = ProduccionProducto.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filter_class = Filtered
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')


class SaboresProduccion(ListAPIView):
    serializer_class = SaboresSerializer
    queryset = Sabores.objects.all()


# sabores disponibles
class DetalleSaborProduccion(ListAPIView):
    serializer_class = ProduccionProductoSerializer

    def get_queryset(self):
        return ProduccionProducto.objects.filter().exclude(gramos=0)


# Buscar y actualizar


class ProduccionBuscar(ListAPIView):
    serializer_class = ProduccionProductoSerializer

    def get_queryset(self):
        producto = self.kwargs['pk']
        return ProduccionProducto.objects.filter(
            id=producto
        )


class UpdateGramosProduccion(RetrieveUpdateAPIView):
    serializer_class = UpdateGramosroduccionSerializer
    queryset = ProduccionProducto.objects.all()


class DetalleProduccion(CreateAPIView):
    serializer_class = DetalleProduccionSerializer
    queryset = DetalleProducion.objects.all()


class BasesProduccionList(ListAPIView):
    serializer_class = BasesProduccionSerializer
    queryset = BasesProduccion.objects.all()


class DetalleBaseList(ListAPIView):
    serializer_class = DetalleBaseSerializer
    queryset = DetalleBase.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')


# registramos la producción realizada en resumen

class ProduccionCreate(CreateAPIView):
    serializer_class = ProduccionSerializer
    queryset = Produccion.objects.all()


class ConsumoProduccionCreate(CreateAPIView):
    serializer_class = ConsumoProduccionSerializer
    queryset = ConsumoProduccion.objects.all()
