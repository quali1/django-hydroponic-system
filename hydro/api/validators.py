from rest_framework.validators import UniqueValidator
from hydro.models import HydroponicSystem

unique_hydroponic_system_name = UniqueValidator(queryset=HydroponicSystem.objects.all(), lookup="iexact")
