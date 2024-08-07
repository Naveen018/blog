from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blog_mod.models import Blog, Category

# Create your views here.


def posts_by_category(request, category_id):
    # Fetch posts by category_id
    posts = Blog.objects.filter(status="Published", category_id=category_id)
    # try:
    #     category = Category.objects.get(id=category_id)
    # except:
    #     return redirect("home")
    # pass
    category = get_object_or_404(Category, id=category_id)
    print(category)
    context = {"posts": posts, "category": category}
    # return HttpResponse(posts)
    return render(request, "category.html", context)
