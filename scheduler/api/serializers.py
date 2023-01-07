from rest_framework import serializers
from .models import Course, MyUser

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'passwd')

class AddUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'user_email', 'passwd')

class AddCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'url', 'duration', 'username')