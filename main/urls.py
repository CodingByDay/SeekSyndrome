
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('project/', views.project, name="project"),
    path('project/<int:id>', views.specific, name="specific"),
    path('about/<int:id>', views.news, name="news")
    



]