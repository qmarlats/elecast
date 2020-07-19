from django.urls import path

from .api_views import (
    ProductionCreateAPIView,
    ProductionDestroyAPIView,
    ProductionRetrieveAPIView,
    ProductionListAPIView,
    ProductionUpdateAPIView,
)

app_name = "productions"

urlpatterns = [
    path("", ProductionListAPIView.as_view(), name="list"),
    path("create/", ProductionCreateAPIView.as_view(), name="create"),
    path("<int:pk>/", ProductionRetrieveAPIView.as_view(), name="detail"),
    path("<int:pk>/update/", ProductionUpdateAPIView.as_view(), name="update"),
    path("<int:pk>/delete/", ProductionDestroyAPIView.as_view(), name="delete"),
]
