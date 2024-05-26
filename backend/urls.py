from django.contrib import admin
from django.urls import path, include
from hydro.api.views import HydroViewSet, MeasurementViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('systems', HydroViewSet, basename='hydro')
router.register('measurements', MeasurementViewSet, basename='measurements')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hydro.urls')),
    path('', include('users.urls'))
]

urlpatterns += router.urls