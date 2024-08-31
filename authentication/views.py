from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer ,CustomTokenObtainPairSerializer ,LogoutSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,) # Everyone's welcome to join !
    serializer_class = UserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer  # Our special recipe for tokens


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
     # Time to say goodbye and invalidate that token
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)

