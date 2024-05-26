from hydro.models import HydroponicSystem
from rest_framework.validators import UniqueValidator

unique_hydroponic_system_name = UniqueValidator(queryset=HydroponicSystem.objects.all(), lookup="iexact")
