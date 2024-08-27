from django.shortcuts import get_object_or_404, redirect, render

from blog_mod.models import Blog, Category
from django.contrib.auth.decorators import login_required

from dashboard.forms import AddUserForm, BlogPostForm, CategoryForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url="login")
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {"category_count": category_count, "blogs_count": blogs_count}
    return render(request, "dashboard/dashboard.html", context)


def categories(request):
    # We can get categories directly from context_processors.py and use it in UI(No need to write code to get categories)
    return render(request, "dashboard/categories.html")


def add_category(request):
    if request.method == "POST":
        # print(request.POST['category_name'])
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("categories")  # if block will end here and will not got to context line
    else:  # This else block is actually not required
        form = CategoryForm()
    context = {"form": form}
    return render(request, "dashboard/add_category.html", context)


def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)  # Passing instance(previous value) is compulsory

        # Why instance=category in POST?
        # When you submit the edited form, the instance=category argument ensures that the updated data is saved to the same category object in the database.
        # Without instance=category, a new category object might be created with the submitted data, leading to duplicate entries.
        if form.is_valid:
            form.save()
            return redirect("categories")
    form = CategoryForm(instance=category)  # Here instance will prepopulate the category name in the form when we click on edit
    context = {"form": form, "category": category}
    return render(request, "dashboard/edit_category.html", context)


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect("categories")


def posts(request):
    posts = Blog.objects.all()  # posts has a list of objects(blog posts)
    context = {"posts": posts}
    return render(request, "dashboard/posts.html", context)


def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        # If we upload images/files in our form all the text data will be stored in request.POST as dict format
        # But the images/files will be stored in request.FILES
        if form.is_valid:
            # To add custom data to the form
            post = form.save(commit=False)  # Here we are temporarily saving the form to post object

            # This post object will have all the fields of Blog model including author and slug(We chose not the include author...
            # ...and slug field in our BlogPostForm to show it in UI but BlogPostForm is based on Blog model which has author field has mandatory field)

            # So before saving the form we are temporarily saving form to post object and adding current logged in user as author and saving it
            # To get current logged in user we use "request.user"
            # Even if we don't give slug the post will be created/saved because we have given slug as optional(blank=True) in our Blog model

            # but we can add only one post without slug, if we try to add another post without slug it gives us error!!! -- This is because
            # slug is an unique constraint and we already had a blank slug for previous post and even for this since slug is not being generated
            # yet it gives us an error saying unique contraint failed for slug
            post.author = request.user
            post.save()  # form.save() also works here
            title = form.cleaned_data["title"]  # This is coming from request.POST which is stored in form
            post.slug = slugify(title) + "-" + str(post.id)  # Only after saving the data we get id of this blog post, hence post.save() is compulsory before creating slug
            post.save()
            # print(post.slug)  This will print [this-is-new] if the title is [this is new]
            return redirect("posts")  # if block will end here and will not got to context line
        else:
            print(form.errors)
    else:  # This else block is actually not required
        form = BlogPostForm()
    context = {"form": form}
    return render(request, "dashboard/add_post.html", context)

# So basically in adding post we are first saving the post so that we get its id and then creating slug for it using the id to make it unique


def edit_post(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)  # Passing instance(previous value) is compulsory

        # Why instance=post in POST?
        # When you submit the edited form, the instance=post argument ensures that the updated data is saved to the same blog post object in the database.
        # Without instance=post, a new blog post object might be created with the submitted data, leading to duplicate entries.
        if form.is_valid:
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect("posts")
    form = BlogPostForm(instance=post)  # Here instance will prepopulate the post details in the form when we click on edit
    context = {"form": form, "post": post}
    return render(request, "dashboard/edit_post.html", context)
# NOTE: We haven't handled updating images in edit_post functionality



def delete_post(request, id):
    post = get_object_or_404(Blog, id=id)
    post.delete()
    return redirect("posts")


def users(request):
    users = User.objects.all()
    context = {
        "users" : users
    }
    return render(request, "dashboard/users.html", context)

def add_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST) 
        # request.POST will hold all the values of form we enter in the UI as dictionary(key-form fields, value-form data)
        if form.is_valid:
            form.save()
            return redirect("users")
        else:
            print(form.errors)
    form = AddUserForm()
    context = {"form" : form}
    return render(request, "dashboard/add_user.html", context)


def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)  # Passing instance(previous value) is compulsory

        # Why instance=user in POST?
        # When you submit the edited form, the instance=user argument ensures that the updated data is saved to the same category object in the database.
        # Without instance=user, a new user object might be created with the submitted data, leading to duplicate entries.
        if form.is_valid:
            form.save()
            return redirect("users")
    form = EditUserForm(instance=user)  # Here instance will prepopulate the user details in the form when we click on edit
    context = {"form": form, "user": user}
    return render(request, "dashboard/edit_user.html", context)


def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect("users")
