from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from hydro.models import HydroponicSystem, Measurement
from .serializers import HydroponicSystemSerializer, MeasurementSerializer
from .filters import HydroponicSystemFilter, MeasurementFilter


class HydroViewSet(viewsets.ModelViewSet):
    """
    get -> list → Queryset
    get -> retrieve → Product Instance Detail View
    post -> create → New Instance
    put -> Update
    patch -> Partial Update
    delete -> destroy
    """

    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HydroponicSystemFilter
    lookup_field = "pk"

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MeasurementViewSet(viewsets.ModelViewSet):
    """
    get -> list → Queryset
    get -> retrieve → Product Instance Detail View
    post -> create → New Instance
    put -> Update
    patch -> Partial Update
    delete -> destroy
    """

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MeasurementFilter
    lookup_field = "pk"

    def get_queryset(self):
        return Measurement.objects.filter(hydroponic_system__owner=self.request.user)

