from django.shortcuts import get_object_or_404, redirect, render

from blog_mod.models import Blog, Category
from django.contrib.auth.decorators import login_required

from dashboard.forms import CategoryForm

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
            return redirect(
                "categories"
            )  # if block will end here and will not got to context line
    else:
        form = CategoryForm()
    context = {"form": form}
    return render(request, "dashboard/add_category.html", context)


def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        form = CategoryForm(
            request.POST, instance=category
        )  # Passing instance(previous value) is compulsory

        # Why instance=category in POST?
        # When you submit the edited form, the instance=category argument ensures that the updated data is saved to the same category object in the database.
        # Without instance=category, a new category object might be created with the submitted data, leading to duplicate entries.
        if form.is_valid:
            form.save()
            return redirect("categories")
    form = CategoryForm(instance=category) # Here instance will prepopulate the category name in the form when we click on edit
    context = {"form": form, "category": category}
    return render(request, "dashboard/edit_category.html", context)


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect("categories")
