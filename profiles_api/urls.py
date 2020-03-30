from django.urls import path
from django.conf.urls import url
from profiles_api import views

urlpatterns = [

path('hello_view/', views.HelloApiView.as_view()),
]
