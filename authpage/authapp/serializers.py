# authapp/serializers.py

from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        u = CustomUser.objects.create(username=validated_data['username'])
        u.set_password(validated_data['password'])
        u.save()
        return u
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        # extra_kwargs = {'password': {'write_only': True}}