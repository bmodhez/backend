from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.utils import timezone
from .models import User, LoginHistory
from .serializers import RegisterSerializer



def get_ip(request):
    x = request.META.get("HTTP_X_FORWARDED_FOR")
    return x.split(",")[0] if x else request.META.get("REMOTE_ADDR")


#User Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Log 
        LoginHistory.objects.create(
            user=user,
            email=user.email,
            login_time=timezone.now(),
            ip_address=get_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", ""),
            success=True,
            failure_reason="Registration"
        )

        return Response({
            "message": "User registered successfully",
            "user": {"id": user.id, "email": user.email, "name": user.name}
        }, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, username=email, password=password)
        ip = get_ip(request)
        user_agent = request.META.get("HTTP_USER_AGENT", "")

        if user:
            LoginHistory.objects.create(
                user=user, email=email,
                ip_address=ip, user_agent=user_agent,
                success=True
            )
            return super().post(request, *args, **kwargs)

  #If user failed to logn
        failure = "Invalid password"
        user_obj = User.objects.filter(email=email).first()

        if not user_obj:
            failure = "User does not exist"

        LoginHistory.objects.create(
            user=user_obj,
            email=email,
            ip_address=ip,
            user_agent=user_agent,
            success=False,
            failure_reason=failure
        )

        return Response(
            {"detail": "Invalid email or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )
