from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class ProfileSreializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSreialzier(serializers.ModelSerializer):
    profile = ProfileSreializer()

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','profile']