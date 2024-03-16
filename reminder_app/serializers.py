from rest_framework import serializers
from .models import Reminder
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name', required=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'email','username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ReminderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Reminder
        fields = ['id', 'user', 'message', 'date', 'time']