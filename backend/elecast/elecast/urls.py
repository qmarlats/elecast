from django.urls import include, path

urlpatterns = [
    path("api/", include("elecast.api_urls", namespace="api")),
]
