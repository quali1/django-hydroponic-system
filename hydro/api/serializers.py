from rest_framework import serializers
from rest_framework.reverse import reverse

from hydro.models import HydroponicSystem, Measurement
from .validators import unique_hydroponic_system_name


class HydroponicSystemSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='hydro-detail', lookup_field='pk')
    name = serializers.CharField(
        validators=[unique_hydroponic_system_name]
    )

    class Meta:
        model = HydroponicSystem
        fields = '__all__'
        read_only_fields = ['owner']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            self.fields['hydroponic_system'].queryset = HydroponicSystem.objects.filter(owner=request.user)

    def validate_ph_level(self, value):
        if value < 0 or value > 14:
            raise serializers.ValidationError("The pH level should be between 0 and 14.")
        return value

    def validate_tds_level(self, value):
        if value < 0:
            raise serializers.ValidationError("The TDS level cannot be negative.")
        return value

    def validate_temperature(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("The temperature should be between 0 and 100 degrees Celsius.")
        return value
