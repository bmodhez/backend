from rest_framework import serializers
from assets.models import Asset
from users.models import User


class AssignedUserMiniSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "display_name")

    def get_display_name(self, obj):
        return obj.name or obj.email


class AssetSerializer(serializers.ModelSerializer):

    test = serializers.SerializerMethodField()

    def get_test(self, obj):
        return "Hi"

    class Meta:
        model = Asset
        fields = "__all__"
