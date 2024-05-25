from rest_framework import generics, mixins

from .models import HydroponicSystem
from .api.serializers import HydroponicSystemSerializer


class HydroponicSystemMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):  # http -> get
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  # http -> post
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


hydroponic_system_mixin_view = HydroponicSystemMixinView.as_view()
