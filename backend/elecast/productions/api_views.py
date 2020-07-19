from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
)

from .models import Production
from .serializers import ProductionSerializer


class ProductionCreateAPIView(CreateAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer


class ProductionDestroyAPIView(DestroyAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer


class ProductionListAPIView(ListAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer


class ProductionUpdateAPIView(UpdateAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer


class ProductionRetrieveAPIView(RetrieveAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
