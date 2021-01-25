from django.shortcuts import render
from .models import Facturas
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from django_filters.rest_framework import (
    DjangoFilterBackend,
)

from .serializers import (
    FacturasSerializer,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)


class FacturaList(ListAPIView):
    serializer_class = FacturasSerializer
    queryset = Facturas.objects.all()


class FacturasAdd(CreateAPIView):

    serializer_class = FacturasSerializer
    queryset = Facturas.objects.all()
