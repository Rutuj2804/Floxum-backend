from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Group
from .serializers import GroupSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from posts.models import Post
from posts.serializers import PostSerializer


class AddGroup(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self,request,format=None):
        data = self.request.data
        name = data['name']
        about = data['about']
        image = data['photo']
        admin = self.request.user
        website = data['website']
        email = data['email']
        facebook = data['facebook']
        instagram = data['instagram']
        Group.objects.create(name=name, admin=admin , about=about, website=website, email=email, instagram=instagram, facebook=facebook, image=image)
        return Response({'success': 'Successfully created Group'})


class AddPost(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self,request,format=None):
        try:
            data = self.request.data
            user = self.request.user
            caption = data['caption']
            Post.objects.create(user=user, caption=caption, group_post=True)
            return Response({'success': 'Successfully created Post'})
        except:
            return Response({'error': 'Something went wrong while posting'})


class GetGroups(APIView):
    authentication_classes = [TokenAuthentication,]

    def get(self,request,format=None):
        try:
            user = self.request.user
            groups = Group.objects.filter(remove=False, members=user)
            serializers = GroupSerializer(groups, many=True)
            return Response({'groups':serializers.data, 'success': 'successfully fetched groups'})
        except:
            return Response({'error': 'Something went wrong while fetching groups'})



class GetGroupDetailView(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self,request,format=None):
        id = self.request.data['id']
        group = Group.objects.get(id=id)
        if not group.remove:
            serializers = GroupSerializer(group)
            return Response({'group':serializers.data, 'success': 'Successfully fetched group'})
        else:
            return Response({'error': 'This group does not exist'})


class DeleteGroupView(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        try:
            data = self.request.data
            id = data['id']
            Group.objects.filter(id=id).update(remove=True)
            return Response({'success': 'Successfully deleted group'})
        except:
            return Response({'error': 'Something went wrong while delete group'})


class AddMemberGroupView(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        try:
            data = self.request.data
            member = data['member']
            id = data['id']
            group = Group.objects.get(id=id)
            if self.request.user == group.admin:
                if User.objects.filter(username=member).exists():
                    user = User.objects.get(username=member)
                    group.members.add(user)
                    return Response({'success': 'Successfully added member'})
                else:
                    return Response({'error': 'No user Exists with this username'})
            else:
                return Response({'error': 'You are not authorized to add members in this group'})
        except:
            return Response({'error': 'Something went wrong while adding member'})


class RemoveMemberGroupView(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        try:
            data = self.request.data
            member = data['member']
            id = data['id']
            group = Group.objects.get(id=id)
            if self.request.user == group.admin:
                if User.objects.filter(username=member).exists():
                    user = User.objects.get(username=member)
                    group.members.add(user)
                    return Response({'success': 'Successfully added member'})
                else:
                    return Response({'error': 'No user Exists with this username'})
            else:
                return Response({'error': 'You are not authorized to add members in this group'})
        except:
            return Response({'error': 'Something went wrong while adding member'})