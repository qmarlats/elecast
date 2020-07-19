from django.urls import path

from .api_views import (
    LocationCreateAPIView,
    LocationDestroyAPIView,
    LocationRetrieveAPIView,
    LocationListAPIView,
    LocationUpdateAPIView,
)

app_name = "locations"

urlpatterns = [
    path("", LocationListAPIView.as_view(), name="list"),
    path("create/", LocationCreateAPIView.as_view(), name="create"),
    path("<int:pk>/", LocationRetrieveAPIView.as_view(), name="detail"),
    path("<int:pk>/update/", LocationUpdateAPIView.as_view(), name="update"),
    path("<int:pk>/delete/", LocationDestroyAPIView.as_view(), name="delete"),
]
