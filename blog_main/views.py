from django.http import HttpResponse
from django.shortcuts import redirect, render

from assignments.models import About, SocialLinks
from blog_main.forms import RegistrationForm
from blog_mod.models import Blog, Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


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


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        # All the data we enter from UI will be kept in request.POST, but we are sending this data to RegistrationForm class for validation purpose
        if form.is_valid():
            form.save()
            return redirect(
                "register"
            )  # redirect will redirect to certain url, so give url name not html name
        else:
            print(form.errors)
    else:
        form = (
            RegistrationForm()
        )  # Initial when register/ url is called it will call this class which gets the form and loads it in UI
    context = {"form": form}
    form_fields = request.POST
    print(form_fields)
    return render(request, "register.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
#This form.cleaned_data wil print the the data we sending from form from UI in dictionary {'username': 'djangoadmin', 'password': 'Nav@3112000'}
            user = auth.authenticate(username=username, password=password)
# This auth.authenticate() will take username and password from the form we are getting and returns the user if uname and passw matches in db
            if user is not None:
                auth.login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
        # AuthenticationForm is the default form for login features provided in django(It has only 2 fields-username and password)
    context = {"form": form}
    return render(request, "login.html", context)

def logout(request):
    auth.logout(request)
    return redirect("home")
