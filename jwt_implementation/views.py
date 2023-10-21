from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from customusers.models import CustomUser  # Import your custom user model

class CustomTokenObtainPairView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Verify user credentials
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Create a new RefreshToken for the user
        refresh_token = RefreshToken.for_user(user)

        # Access the access token and refresh token tokens
        access_token = str(refresh_token.access_token)
        refresh_token = str(refresh_token)

        return Response({
            'access_token': access_token,
            'refresh_token': refresh_token,
        })
