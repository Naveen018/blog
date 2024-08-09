from django.http import HttpResponse
from django.shortcuts import render

from assignments.models import About, SocialLinks
from blog_mod.models import Blog, Category


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by(
        "-updated_at"
    )
    unfeatured_posts = Blog.objects.filter(is_featured=False, status="Published")
    # Fetch about us
    about_us = About.objects.get()
    context = {
        "featured_post": featured_posts,
        "unfeatured_post": unfeatured_posts,
        "about": about_us,
    }
    return render(request, "home.html", context)


# Filter - Returns a QuerySet object containing all objects that match the given lookup parameters
#        - Use for loop to access each objects and their fields (for post in featured_posts: post.title)
# Get - Returns a single object that matches the given lookup parameters.
#     - Use object variable directly to access their fields (about_us.description)
