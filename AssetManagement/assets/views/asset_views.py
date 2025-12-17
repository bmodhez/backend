from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from assets.models import Asset
from django.shortcuts import render, redirect
from assets.serializers import AssetSerializer
from assets.permissions import IsStaffOrReadOnly

class AssetViewSet(ModelViewSet):
    queryset = Asset.objects.all().order_by("-created_at")
    serializer_class = AssetSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]

    def perform_create(self, serializer):
        asset = serializer.save()
        if asset.assigned_to:
            asset.status = "deployed"
            asset.save()

    def perform_update(self, serializer):
        serializer.save()

def assigned(request):
    assets = Asset.objects.all()              # 1. get data
    serializer = AssetSerializer(assets, many=True)  # 2. instantiate serializer

    for item in serializer.data:               # 3. access data
        for key, value in item.items():
            print(f"{key}: {value}")
            
    return render(request, "hi.html")