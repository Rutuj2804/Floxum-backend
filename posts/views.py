from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, PostImages
from .serializers import PostSerializer, ImagesSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from groups.models import Group
from groups.serializers import GroupSerializer
from user_profile.serializers import UserProfileSerializer


class AddPost(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self,request,format=None):
        try:
            data = self.request.data
            user = self.request.user
            caption = data['caption']
            group = data['group']
            image_one = data['image_1']
            image_two = data['image_2']
            image_three = data['image_3']
            image_four = data['image_4']
            image_five = data['image_5']
            image_six = data['image_6']
            image_seven = data['image_7']
            images = PostImages.objects.create(image_1=image_one, image_2=image_two, image_3=image_three, image_4=image_four,image_5=image_five, image_6=image_six, image_7=image_seven)
            user_profile = UserProfile.objects.get(user=user)
            group = Group.objects.get(id=group)
            post = Post.objects.create(user=user, caption=caption, user_profile=user_profile, group_of_post=group)
            post.images.add(images)
            serializer = PostSerializer(post)
            return Response({'success': 'Successfully created Post', 'post': serializer.data})
        except:
            return Response({'error': 'Something went wrong while posting'})


class GetPosts(APIView):
    authentication_classes = [TokenAuthentication,]

    def get(self,request,format=None):
        user = self.request.user
        myprofile = UserProfile.objects.get(user=user.id)
        array = []
        for user in myprofile.followers.all():
            posts = Post.objects.filter(remove=False, user=user.id)
            for post in posts:
                user_profile = UserProfileSerializer(post.user_profile).data
                images = ImagesSerializer(post.images, many=True).data
                group = GroupSerializer(post.group_of_post).data
                serailizer = {
                    "id": post.id,
                    "caption": post.caption,
                    "create_date": post.create_date,
                    "create_Time": post.create_Time,
                    "like": post.like.all().count(),
                    "isLiked": post.like.filter(username=post.user).exists(),
                    "group_post": post.group_post,
                    "images": images,
                    "user_profile": user_profile,
                    "group_of_post": group
                }
                array.append(serailizer)
        myposts = Post.objects.filter(user=self.request.user)
        for mypost in myposts:
            images = ImagesSerializer(mypost.images, many=True).data
            user_profile = UserProfileSerializer(post.user_profile).data
            group = GroupSerializer(post.group_of_post).data
            serail = {
                "id": mypost.id,
                "caption": mypost.caption,
                "create_date": mypost.create_date,
                "create_Time": mypost.create_Time,
                "like": mypost.like.all().count(),
                "isLiked": mypost.like.filter(username=mypost.user.username).exists(),
                "group_post": mypost.group_post,
                "images": images,
                "user_profile": user_profile,
                "group_of_post": group
            }
            array.append(serail)
        return Response({'success': 'successfully fetched posts', 'posts': array})


class GetMyPosts(APIView):
    authentication_classes = [TokenAuthentication,]

    def get(self, request, format=None):
        user = self.request.user
        mypost = Post.objects.filter(user=user.id, remove=False)
        serializer = PostSerializer(mypost, many=True)
        return Response({'success': 'Posts fetched successfully', 'posts': serializer.data})


class GetGroupPosts(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        try:
            data = self.request.data['id']
            mypost = Post.objects.filter(group_of_post=data, remove=False)
            serializer = PostSerializer(mypost, many=True)
            return Response({'success': 'Posts fetched successfully', 'posts': serializer.data})
        except:
            return Response({'error': 'Something went wrong'})


class GetPostDetailView(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self,request,format=None):
        id = self.request.data['id']
        post = Post.objects.get(id=id)
        if not post.remove:
            userprofile = UserProfileSerializer(post.user_profile).data
            group = GroupSerializer(post.group_of_post).data
            array = []
            for image in post.images.all():
                if image.image_1:
                    array.append({'image': '/media/'+str(image.image_1)})
                if image.image_2:
                    array.append({'image': '/media/'+str(image.image_2)})
                if image.image_3:
                    array.append({'image': '/media/'+str(image.image_3)})
                if image.image_4:
                    array.append({'image': '/media/'+str(image.image_4)})
                if image.image_5:
                    array.append({'image': '/media/'+str(image.image_5)})
                if image.image_6:
                    array.append({'image': '/media/'+str(image.image_6)})
                if image.image_7:
                    array.append({'image': '/media/'+str(image.image_7)})
            serializers = {
                'id': post.id,
                'caption': post.caption,
                'create_date': post.create_date,
                'create_Time': post.create_Time,
                'group_post': post.group_post,
                'user_profile': userprofile,
                'group_of_post': group,
                'like': post.like.all().count(),
                'images': array
            }
            return Response({'success':'post fetched successfully', 'posts':serializers})
        else:
            return Response({'error': 'This POST does not exist'})


class DeletePostView(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        try:
            data = self.request.data
            id = data['id']
            Post.objects.filter(id=id).update(remove=True)
            return Response({'success': 'Successfully deleted post'})
        except:
            return Response({'error': 'Something went wrong while delete post'})


class AddLikePostView(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        try:
            data = self.request.data
            user = self.request.user
            id = data['id']
            if Post.objects.filter(id=id).exists():
                post = Post.objects.get(id=id)
                user = User.objects.get(username=user)
                if post.like.filter(username=user).exists():
                    post.like.remove(user)
                    return Response({'success': 'Successfully unlike'})
                else:
                    post.like.add(user)
                    return Response({'success': 'Successfully added like'})
            else:
                return Response({'error': 'No post Exists with this id'})
        except:
            return Response({'error': 'Something went wrong while adding member'})




class AddCommentPostView(APIView):
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        pass