from django.contrib import admin
from django.urls import path
from tags.views import CraeteTagAPiView, TagDetailViewV1, TagDetailViewV2

urlpatterns = [
    path('create/', CraeteTagAPiView.as_view(), name='create-tag'),
    path('tag-detail/v1/<str:slug>', TagDetailViewV1.as_view(), name='tag-detail-v1'),
    path('tag-detail/v2/<str:slug>', TagDetailViewV2.as_view(), name='tag-detail-v2'),
]