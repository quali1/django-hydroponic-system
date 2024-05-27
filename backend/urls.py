from django.contrib import admin
from django.urls import path, include
from hydro.api.views import HydroViewSet, MeasurementViewSet
from rest_framework import routers
from rest_framework.permissions import IsAuthenticated
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('systems', HydroViewSet, basename='hydro')
router.register('measurements', MeasurementViewSet, basename='measurements')

schema_view = get_schema_view(
    openapi.Info(
        title="Hydroponic System API",
        default_version='v1',
        description="""
        This API allows users to manage their hydroponic systems efficiently,
        enabling creation, reading, updating, and deletion (CRUD) of system information,
        as well as handling sensor data measurements such as pH, water temperature, and TDS. 
        This documentation provides detailed instructions on how to interact with our endpoints.
        """,
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('hydro.urls')),
    path('', include('users.urls')),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/', schema_view.with_ui('redoc', cache_timeout=0), name='api-docs'),
    path('api/swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
