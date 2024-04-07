from django.contrib import admin
from django.urls import path
from tags.views import CraeteTagAPiView 

urlpatterns = [
    path('create/', CraeteTagAPiView.as_view(), name='create-tag'),
]