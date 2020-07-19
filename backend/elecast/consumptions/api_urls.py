from django.urls import path

from .api_views import (
    ConsumptionCreateAPIView,
    ConsumptionDestroyAPIView,
    ConsumptionRetrieveAPIView,
    ConsumptionListAPIView,
    ConsumptionUpdateAPIView,
)

app_name = "consumptions"

urlpatterns = [
    path("", ConsumptionListAPIView.as_view(), name="list"),
    path("create/", ConsumptionCreateAPIView.as_view(), name="create"),
    path("<int:pk>/", ConsumptionRetrieveAPIView.as_view(), name="detail"),
    path("<int:pk>/update/", ConsumptionUpdateAPIView.as_view(), name="update"),
    path("<int:pk>/delete/", ConsumptionDestroyAPIView.as_view(), name="delete"),
]
