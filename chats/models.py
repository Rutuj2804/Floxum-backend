from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.TextField()
    image = models.FileField(upload_to='chats', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Thread(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
    messages = models.ManyToManyField(Message)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user1.username + self.user2.username