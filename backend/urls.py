from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auths.urls')),
    path('rest_auth_links/', obtain_auth_token),
    path('groups/', include('groups.urls')),
    path('chats/', include('chats.urls')),
    path('events/', include('events.urls')),
    path('posts/', include('posts.urls')),
    path('user_profile/', include('user_profile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
