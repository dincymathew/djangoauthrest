from django.shortcuts import render

# Create your views here.


# authapp/views.py

from rest_framework import generics, status,viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Password strength validation
        password = request.data.get('password', '')
        if not (len(password) >= 8 and any(c.isupper() for c in password) and any(c.isascii() and not c.isalnum() for c in password)):
            return Response({'error': 'Password must be at least 8 characters with at least 1 uppercase letter and 1 special character.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

class UserLoginView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        user = CustomUser.objects.filter(email=email).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

class userviewset(viewsets.ModelViewSet):

    queryset=CustomUser.objects.all()
    serializer_class = UserSerializer
