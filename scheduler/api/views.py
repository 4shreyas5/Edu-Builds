from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import AddUserSerializer, LoginUserSerializer, AddCourseSerializer

from .models import MyUser, Course


class AddUserView(APIView):
    serializer_class = AddUserSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Then add the user to the database
            username = serializer.data['username']
            user_email = serializer.data['user_email']
            passwd = serializer.data['passwd']

            # Create a new user with these fields
            user = MyUser(username=username, user_email=user_email, passwd=passwd)
            user.save()

        return Response(AddUserSerializer(user).data, status=status.HTTP_201_CREATED)


class AddCourseView(APIView):
    serializer_class = AddCourseSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Then add the course to the database
            course_name = serializer.data['name']
            course_url = serializer.data['url']
            course_duration = serializer.data['duration']
            # We get the username of the user
            course_username = serializer.data['username']
            
            # Create a new course with these fields
            course = Course(name=course_name, url=course_url, duration=course_duration, username=course_username)
            course.save()
        
        return Response(AddCourseSerializer(course).data, status=status.HTTP_201_CREATED)
