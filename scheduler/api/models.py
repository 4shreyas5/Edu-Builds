from django.db import models

# Model to handle the Users
class MyUsers(models.Model):
    """
    User will have a username and a passwd
    """
    username = models.CharField(null=False, max_length=20, unique=True)
    user_email = models.EmailField(null=False) 
    passwd = models.CharField(null=False, max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

# Model to handle the users
class Courses(models.Model):
    """
    Courses will contain the information on:
    course-name
    course-url
    course-duration
    course-user
    """
    name = models.CharField(null=False, max_length=50)
    url = models.CharField(null=False, max_length=200)
    duration = models.IntegerField(null=False)
    user_id = models.ForeignKey(MyUsers, null=False, on_delete=models.CASCADE)