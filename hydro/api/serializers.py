from rest_framework import serializers
from rest_framework.reverse import reverse

from hydro.models import HydroponicSystem
from . import validators


class HydroponicSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicSystem
        fields = '__all__'
        read_only_fields = ['owner']