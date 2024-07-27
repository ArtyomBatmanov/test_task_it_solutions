from rest_framework import serializers
from .models import Advertisement
from django.contrib.auth.models import User


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ("id", "title", "author", "views_count", "position")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]
