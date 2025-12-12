from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Asset
from .serializers import AssetSerializer 


class AssetViewSet(ModelViewSet):
    
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [IsAuthenticated]

    def has_staff_permission(self, request):
        return request.user.is_staff

    def create(self, request, *args, **kwargs):
        print(self)
        if not self.has_staff_permission(request):
            return Response({"detail": "Staff only"}, status=403)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not self.has_staff_permission(request):
            return Response({"detail": "Staff only"}, status=403)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not self.has_staff_permission(request):
            return Response({"detail": "Staff only"}, status=403)
        return super().destroy(request, *args, **kwargs)
