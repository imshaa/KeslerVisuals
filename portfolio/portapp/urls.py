from django.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('graphic/', views.graphic, name='graphic'),
    path('figma/', views.figma, name='figma'),
    path('video/', views.video, name='video'),
]
