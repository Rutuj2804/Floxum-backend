from django.urls import path
from .views import AddEventView, GetEventView, DeleteEventView, GetEventDetailView

urlpatterns = [
    path('add/', AddEventView.as_view()),
    path('get/', GetEventView.as_view()),
    path('get-detail/', GetEventDetailView.as_view()),
    path('delete/', DeleteEventView.as_view()),
]