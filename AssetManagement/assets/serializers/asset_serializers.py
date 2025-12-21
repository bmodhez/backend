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

    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        allow_null=True,
        required=False
    )

    assigned_to_detail = AssignedUserMiniSerializer(
        source="assigned_to",
        read_only=True
    )

    class Meta:
        model = Asset
        fields = "__all__"
