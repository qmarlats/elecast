from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
)

from .models import Consumption
from .serializers import ConsumptionSerializer


class ConsumptionCreateAPIView(CreateAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer


class ConsumptionDestroyAPIView(DestroyAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer


class ConsumptionListAPIView(ListAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer


class ConsumptionUpdateAPIView(UpdateAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer


class ConsumptionRetrieveAPIView(RetrieveAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer
