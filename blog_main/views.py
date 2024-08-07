from django.http import HttpResponse
from django.shortcuts import render

from blog_mod.models import Blog, Category


def home(request):
    featured_posts = Blog.objects.filter(is_featured = True, status="Published").order_by("-updated_at")
    unfeatured_posts = Blog.objects.filter(is_featured = False, status="Published")
    print(featured_posts)
    print(unfeatured_posts)
    context = {
        "featured_post" : featured_posts,
        "unfeatured_post" : unfeatured_posts
    }
    return render(request, "home.html", context)