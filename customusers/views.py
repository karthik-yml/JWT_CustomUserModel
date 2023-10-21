from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from . serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth
from django.contrib.auth import authenticate, login, get_user_model
# Create your views here.
from django.http import JsonResponse

class RegisterUsers(GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request):
    data=self.get_serializer(data=request.data)
    if data.is_valid():
      data.save()
      return Response({'message': 'User registered successfully.'})
    return Response(data.errors)

class LoginAPI(APIView):
    permission_classes = [AllowAny]  

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({'message': 'Login successful.', 'access_token': access_token})
        return Response({'message': 'Login failed.'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        auth.logout(request)
        return Response({'message': 'Logout successful.'})

