from rest_framework import viewsets, mixins, serializers

from api.models import RiskType, DataField


class DataFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataField
        fields = '__all__'

    read_enum_values = serializers.JSONField(source='get_enum_values')


class RiskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskType
        fields = '__all__'

    fields = DataFieldSerializer(many=True)


class RiskTypeViewSet(viewsets.ModelViewSet):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
