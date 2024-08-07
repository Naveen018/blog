
from django.contrib import admin
from django.urls import include, path

from blog_mod import views

urlpatterns = [
    path("<int:category_id>/",views.posts_by_category, name = "posts_by_category")
]