from django.urls import path
from .views import GetUserViewSet, RegisterUserViewSet, CheckAuthentication, LoadUserViewSet

urlpatterns = [
    path('getall/', GetUserViewSet.as_view()),
    path('register/', RegisterUserViewSet.as_view()),
    path('authentication/', CheckAuthentication.as_view()),
    path('load_user/', LoadUserViewSet.as_view()),
]
