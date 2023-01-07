from django.urls import path
from .views import AddUserView, AddCourseView

urlpatterns = [
    path('add-user/', AddUserView.as_view()),
    path('add-course/', AddCourseView.as_view())
]
