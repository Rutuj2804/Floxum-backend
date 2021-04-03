from rest_framework.views import APIView
from .models import UserProfile, Timeline
from .serializers import UserProfileSerializer, TimelineSerailizer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.permissions import AllowAny
from auths.serializers import UserSerializer


class GetUserViewSet(APIView):
    authentication_classes = [TokenAuthentication,]

    def get(self, request, format=None):
        try:
            user = self.request.user
            userprofile = UserProfile.objects.get(user=user)
            user = UserSerializer(user).data
            image = userprofile.image
            serializer = {
                'user': user,
                'tagline': userprofile.tagline,
                'about_me': userprofile.about_me,
                'facebook': userprofile.facebook,
                'instagram': userprofile.instagram,
                'image': '/media/'+str(image),
                'followers': userprofile.followers.all().count(),
                'following': userprofile.following.all().count(),
            }
            return Response({'success': 'Successfully fetched user data', 'user': serializer})
        except:
            return Response({'error': 'Something went wrong while fetching user data'})


class GetAllUsersViewSet(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        try:
            userprofile = UserProfile.objects.all()
            serializer = UserProfileSerializer(userprofile, many=True)
            return Response(serializer.data)
        except:
            return Response({'error': 'Something went wrong while fetching user data'})



class EditProfileViewSet(APIView):
    authentication_classes = [TokenAuthentication,]

    def put(self, request, format=None):
        try:
            data = self.request.data
            first_name = data['first_name']
            last_name = data['last_name']
            username = data['username']
            email = data['email']
            tagline = data['tagline']
            about_me = data['about_me']
            instagram = data['instagram']
            facebook = data['facebook']
            image = data['image']
            user = self.request.user
            User.objects.filter(username=user).update(first_name=first_name, last_name=last_name, username=username, email=email)
            userprofile = UserProfile.objects.get(user=user)
            userprofile.tagline = tagline
            userprofile.about_me = about_me
            userprofile.instagram = instagram
            userprofile.facebook = facebook
            userprofile.image = image
            userprofile.save()
            return Response({'success': 'Successfully edited users profile'})
        except:
            return Response({'error': 'Something went wrong while editing users profile'})


class GetProfileViewSet(APIView):
    authentication_classes = [TokenAuthentication,]

    def get(self, request, format=None):
        try:
            user = self.request.user
            userprofile = UserProfile.objects.get(user=user)
            serializer = UserProfileSerializer(userprofile)
            return Response({'success': 'Successfully fetched users profile', 'userprofile': serializer.data})
        except:
            return Response({'error': 'Something went wrong while fetching users profile'})


class GetPersonProfileViewSet(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        try:
            user = self.request.data['user']
            if User.objects.filter(username=user).exists():
                user = User.objects.get(username=user)
                userprofile = UserProfile.objects.get(user=user.id)
                serializer = UserProfileSerializer(userprofile)
                return Response({'success': 'Successfully fetched users profile', 'userprofile': serializer.data})
            else:
                return Response({'error': 'User Not present'}, status=HTTP_404_NOT_FOUND)
        except:
            return Response({'error': 'Something went wrong while fetching users profile'})


class FollowViewSet(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        # try:
        id = self.request.data['id']
        user = self.request.user
        if UserProfile.objects.filter(id=id).exists():
            userprofile = UserProfile.objects.get(id=id)
            if user == userprofile.user:
                return Response({'error': 'cannot process self follow'})
            else:
                me = UserProfile.objects.get(user=user)
                if userprofile.followers.filter(user=user.id).exists():
                    userprofile.followers.remove(user)
                    me.following.remove(userprofile.user)
                    return Response({'success': 'Successfully unfollowed user'})
                else:
                    userprofile.followers.add(user)
                    me.following.add(userprofile.user)
                    return Response({'success': 'Successfully followed users'})
        else:
            return Response({'error': 'User does not exists'})
        # except:
        #     return Response({'error': 'Something went wrong while following users'})



class UnFollowViewSet(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        try:
            id = self.request.data['id']
            user = self.request.user
            if UserProfile.objects.filter(id=id).exists():
                userprofile = UserProfile.objects.get(id=id)
                if user == userprofile.user:
                    return Response({'error': 'cannot process self unfollow'})
                else:
                    userprofile.followers.remove(user)
                    return Response({'success': 'Successfully unfollowed users'})
            else:
                return Response({'error': 'User does not exists'})
        except:
            return Response({'error': 'Something went wrong while following users'})


class AddTimelineViewSet(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        try:
            data = self.request.data
            user = self.request.user
            image = data['image']
            text = data['text']
            title = data['title']
            date = data['date']
            timeline_instance = Timeline.objects.create(image=image, text=text, date=date, title=title)
            userprofile = UserProfile.objects.get(user=user)
            userprofile.timeline.add(timeline_instance)
            return Response({'success': 'Successfully added timeline'})
        except:
            return Response({'error': 'Something went wrong while adding timeline'})


class GetTimelineViewSet(APIView):
    authentication_classes = [TokenAuthentication,]

    def get(self, request, format=None):
        try:
            user = self.request.user
            userprofile = UserProfile.objects.get(user=user)
            timelines = userprofile.timeline.filter(remove=False)
            serializer = TimelineSerailizer(timelines, many=True)
            return Response({'success': 'Successfully fetched timelines', 'timelines': serializer.data})
        except:
            return Response({'error': 'Something went wrong while adding timeline'})




class DeleteTimelineViewSet(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        try:
            user = self.request.user
            id = self.request.data['id']
            userprofile = UserProfile.objects.get(user=user)
            userprofile.timeline.filter(id=id).update(remove=True)
            return Response({'success': 'Successfully deleted timelines'})
        except:
            return Response({'error': 'Something went wrong while adding timeline'})