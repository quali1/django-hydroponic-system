from rest_framework import viewsets

from hydro.models import HydroponicSystem, Measurement
from .serializers import HydroponicSystemSerializer, MeasurementSerializer


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
    lookup_field = "pk"

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
    lookup_field = "pk"

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


