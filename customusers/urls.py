from django.urls import path, include
from . views import RegisterUsers, LoginAPI, LogoutAPI

urlpatterns = [
  path('register/',RegisterUsers.as_view()),
  path('login/', LoginAPI.as_view()),
  path('logout/', LogoutAPI.as_view())
]