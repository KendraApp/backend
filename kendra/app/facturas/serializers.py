from rest_framework import serializers
from .models import Facturas


class FacturasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Facturas
        fields = ('__all__')
