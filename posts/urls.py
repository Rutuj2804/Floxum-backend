from django.urls import path
from .views import AddPost, AddLikePostView, DeletePostView, GetPosts, GetPostDetailView, AddCommentPostView, GetMyPosts, GetGroupPosts

urlpatterns = [
    path('add/', AddPost.as_view()),
    path('like/', AddLikePostView.as_view()),
    path('delete/', DeletePostView.as_view()),
    path('posts/', GetPosts.as_view()),
    path('my-posts/', GetMyPosts.as_view()),
    path('group-posts/', GetGroupPosts.as_view()),
    path('post-detail/', GetPostDetailView.as_view()),
    path('comment/', AddCommentPostView.as_view()),
]
