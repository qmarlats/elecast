from rest_framework import serializers

from .models import Consumption


class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumption
        fields = "__all__"
