from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("locations/", include("locations.api_urls", namespace="locations")),
    path("consumptions/", include("consumptions.api_urls", namespace="consumptions")),
    path("productions/", include("productions.api_urls", namespace="productions")),
]
