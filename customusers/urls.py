from django.urls import path, include
from . views import RegisterUsers

urlpatterns = [
  path('register/',RegisterUsers.as_view())
]