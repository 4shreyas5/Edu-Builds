from django.urls import path
from .views import fetch_form

urlpatterns = [
    path('form-submit/', fetch_form)
]
