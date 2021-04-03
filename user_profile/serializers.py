from rest_framework import serializers
from .models import UserProfile, Timeline


class TimelineSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        depth = 1