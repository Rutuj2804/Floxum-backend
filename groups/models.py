from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=500)
    admin= models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='admin')
    image = models.ImageField(upload_to='groups', null=True)
    about = models.TextField()
    website = models.CharField(max_length=500)
    email = models.TextField()
    instagram = models.CharField(max_length=500)
    facebook = models.CharField(max_length=500)
    members = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    privacy = models.BooleanField(default=False)
    display_social = models.BooleanField(default=False)
    remove = models.BooleanField(default=False)

    def __str__(self):
        return self.name