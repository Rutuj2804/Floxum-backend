from django.db import models
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from groups.models import Group

class PostImages(models.Model):
    image_1 = models.FileField('posts', null=True)
    image_2 = models.FileField('posts', null=True)
    image_3 = models.FileField('posts', null=True)
    image_4 = models.FileField('posts', null=True)
    image_5 = models.FileField('posts', null=True)
    image_6 = models.FileField('posts', null=True)
    image_7 = models.FileField('posts', null=True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    create_Time = models.TimeField(auto_now_add=True)
    like = models.ManyToManyField(User, related_name='Likes')
    remove = models.BooleanField(default=False)
    group_post = models.BooleanField(default=False)
    images = models.ManyToManyField(PostImages)
    user_profile = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
    group_of_post = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    # report = models.ManyToManyField(Reports)
    # comment = models.ManyToManyField(User, related_name='Likes')

