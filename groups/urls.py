from django.urls import path
from .views import AddGroup, GetGroups, DeleteGroupView, AddMemberGroupView, GetGroupDetailView, AddPost

urlpatterns = [
    path('add/', AddGroup.as_view()),
    path('get/', GetGroups.as_view()),
    path('post/', AddPost.as_view()),
    path('group-detail/', GetGroupDetailView.as_view()),
    path('delete/', DeleteGroupView.as_view()),
    path('add-member/', AddMemberGroupView.as_view()),
]