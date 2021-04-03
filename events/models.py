from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=500)
    desc_one = models.TextField()
    desc_two = models.TextField()
    location = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    contact = models.IntegerField()
    link = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_one = models.ImageField(upload_to='events', null=True)
    image_two = models.ImageField(upload_to='events', null=True)
    image_three = models.ImageField(upload_to='events', null=True)
    remove = models.BooleanField(default=False)

    def __str__(self):
        return self.title