#import django_filters
from django.shortcuts import render

from .models import (
    Insumos,
    Compras,
    Unidad_Medida,
    ConsumoInsumo
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
    InsumosSerializer,
    UnidadMedidaSerializer,
    ShopInsumosSerializer,
    AddShopInsumosSerializer,
    UpdateGramosInsumosSerializer,
    ConsumoInsumoSerializer
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)


class ConsumoList(ListAPIView):
    serializer_class = ConsumoInsumoSerializer
    queryset = ConsumoInsumo.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = [
        'id',
        'nombre',
    ]
    search_fields = ('__all__')
    ordering_fields = ('__all__')


class ConsumoCreate(CreateAPIView):
    serializer_class = ConsumoInsumoSerializer
    queryset = ConsumoInsumo.objects.all()


class ListUnidadMedida(ListAPIView):
    serializer_class = UnidadMedidaSerializer
    queryset = Unidad_Medida.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = [
        'id',
        'nombre',
    ]
    search_fields = ('__all__')
    ordering_fields = ('__all__')


class Filtered(FilterSet):
    negated_gramos__not = filters.NumberFilter(
        field_name='gramos', exclude=True)

    class Meta:
        model = Insumos
        fields = ('__all__')


class ListInsumos(ListAPIView):
    serializer_class = InsumosSerializer
    queryset = Insumos.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filter_class = Filtered
    filterset_fields = [
        'id',
        'nombre',
        'gramos',
    ]
    search_fields = [
        'nombre',
        'gramos',
    ]
    ordering_fields = (
        'id',
        'nombre',
        'modified',
    )


class CompraInsumos(ListAPIView):
    serializer_class = ShopInsumosSerializer
    queryset = Compras.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = [
        'id',
        'gramos',
        'fecha',
        'precio',
    ]
    search_fields = [
        'insumo__nombre',
    ]
    ordering_fields = (
        'id',
        'fecha',
        'precio',
        'gramos',
    )


class AddCompraInsumos(CreateAPIView):
    serializer_class = AddShopInsumosSerializer
    queryset = Compras.objects.all()

# Buscar y actualizar


class InsumosBuscar(ListAPIView):
    serializer_class = InsumosSerializer

    def get_queryset(self):
        insumos = self.kwargs['pk']
        return Insumos.objects.filter(
            id=insumos
        )


class UpdateGramosInsumos(RetrieveUpdateAPIView):
    serializer_class = UpdateGramosInsumosSerializer
    queryset = Insumos.objects.all()
