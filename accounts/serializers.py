from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class ProfileSreializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True) 
    class Meta:
        model = Profile
        fields = '__all__'

class UserSreialzier(serializers.ModelSerializer):
    profile = ProfileSreializer()

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','profile']
    
    def update(self, instance, validated_data):
       
        profile_data = validated_data.pop('profile', {})
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile = instance.profile
        profile.image = profile_data.get('image', profile.image)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.save()

        return instance
