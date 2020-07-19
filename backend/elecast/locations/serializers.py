from rest_framework import serializers

from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
    
    def to_internal_value(self, data):
        if data.get("latitude", None) == "":
            data["latitude"] = None
        
        if data.get("longitude", None) == "":
            data["longitude"] = None

        return super().to_internal_value(data)
