from rest_framework import serializers
from rest_framework.reverse import reverse

from hydro.models import HydroponicSystem
from .validators import unique_hydroponic_system_name


class HydroponicSystemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[unique_hydroponic_system_name]
    )

    class Meta:
        model = HydroponicSystem
        fields = '__all__'
        read_only_fields = ['owner']
