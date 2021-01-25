from rest_framework import serializers
from .models import Personas


class PersonasSerializer(serializers.ModelSerializer):
    # persona = PersonasSerializer()

    class Meta:
        model = Personas
        fields = ('__all__')
