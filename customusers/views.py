from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from . serializers import RegisterSerializer
# Create your views here.

class RegisterUsers(GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request):
    data=self.get_serializer(data=request.data)
    if data.is_valid():
      data.save()
      return Response({'message': 'User registered successfully.'})
    return Response(data.errors)