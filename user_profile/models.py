from django.db import models
from django.contrib.auth.models import User


class Timeline(models.Model):
    image = models.ImageField(upload_to='timeline', null=True)
    title = models.CharField(max_length=500, null=True)
    text = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    remove = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user', null=True)
    followers = models.ManyToManyField(User, related_name='followers')
    following = models.ManyToManyField(User, related_name='following')
    tagline = models.TextField()
    about_me = models.TextField()
    instagram = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    timeline = models.ManyToManyField(Timeline)

    def __str__(self):
        return self.user.username