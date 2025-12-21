from rest_framework import serializers
from assets.models import Consumable


class ConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumable
        fields = "__all__"
