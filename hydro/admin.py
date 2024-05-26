from django.contrib import admin
from .models import Measurement, HydroponicSystem
# Register your models here.

admin.site.register(Measurement)
admin.site.register(HydroponicSystem)