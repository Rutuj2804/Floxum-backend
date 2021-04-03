from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_profile.models import UserProfile


class GetUserViewSet(APIView):
    permission_classes = [AllowAny,]

    def get(self, request, format=None):
        users = User.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response(serializers.data)


class CheckAuthentication(APIView):
    permission_classes = [AllowAny,]

    def get(self, request, format=None):
        try:
            user = self.request.user
            if User.objects.filter(username=user).exists():
                return Response({'success': 'IsAuthenticated'})
            else:
                return Response({'error': 'Not Authenticated'})
        except:
            return Response({'error': 'Not Authenticated'})


class RegisterUserViewSet(APIView):
    permission_classes = [AllowAny,]

    def post(self, request, format=None):
        data = self.request.data
        try:
            first_name = data['first_name']
            last_name = data['last_name']
            username = data['username']
            password = data['password']
            re_password = data['re_password']
            print(data)
            if password == re_password:
                if first_name != '' and last_name != '' and username !='':
                    if User.objects.filter(username=username).exists():
                        return Response({'error': 'user already exists'})
                    else:
                        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password)
                        UserProfile.objects.create(user=user, tagline='', about_me='')
                        Token.objects.create(user=user)
                        return Response({'success': 'Successfully created user'})
                else:
                    return Response({'error': 'Each field is necessary'})
            else:
                return Response({'error': 'passwords do not match'})
        except:
            return Response({'error': 'something went wrong while registering user'})



class LoadUserViewSet(APIView):

    def get(self, request, format=None):
        user = self.request.user
        try:
            if User.objects.filter(username=user).exists():
                userObject = User.objects.get(username = user)
                serializer = UserSerializer(userObject)
                return Response({'success': 'User Found successfully', 'user': serializer.data})
            else:
                return Response({'error': 'User Does not exists'})
        except:
            return Response({'error': 'Something went wrong while loading user'})
