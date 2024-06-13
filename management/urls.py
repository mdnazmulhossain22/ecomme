from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('contacts/', contact, name="contact"),
    path('contacts/detail/<int:id>', detail, name="detail"),
    path('about/', about, name="about"),
]