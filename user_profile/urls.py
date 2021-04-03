from django.urls import path
from .views import EditProfileViewSet, GetProfileViewSet, FollowViewSet, UnFollowViewSet, GetUserViewSet, AddTimelineViewSet, GetTimelineViewSet, DeleteTimelineViewSet, GetPersonProfileViewSet, GetAllUsersViewSet

urlpatterns = [
    path('edit/', EditProfileViewSet.as_view()),
    path('get/', GetProfileViewSet.as_view()),
    path('getall/', GetAllUsersViewSet.as_view()),
    path('get-person/', GetPersonProfileViewSet.as_view()),
    path('follow/', FollowViewSet.as_view()),
    path('unfollow/', UnFollowViewSet.as_view()),
    path('user/', GetUserViewSet.as_view()),
    path('add-timeline/', AddTimelineViewSet.as_view()),
    path('get-timeline/', GetTimelineViewSet.as_view()),
    path('delete-timeline/', DeleteTimelineViewSet.as_view()),
]