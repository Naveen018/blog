from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blog_mod.models import Blog, Category
from django.db.models import Q

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
    context = {"posts": posts, "category": category}
    # return HttpResponse(posts)
    return render(request, "category.html", context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status="Published")
    context = {"single_blog": single_blog}
    return render(request, "blogs.html", context)


def search(request):
    keyword = request.GET.get(
        "keyword"
    )  # This 'keyword' is the variable in which our search word is stored and sent to views from UI
    # Data transfer from UI to views or vice-versa in django happens through dictionary only(QueryDict)
    blogs = Blog.objects.filter(
        Q(title__icontains=keyword)
        | Q(short_description__icontains=keyword)
        | Q(blog_body__icontains=keyword),
        status="Published",
    )
    # __contains - case sensitive, __icontains = case insensitive
    # , inside filter will be considered as and operator
    #  Q provide a way to combine multiple lookup expressions(title,description) using logical operators (AND, OR, NOT)
    print(blogs)
    context = {"blogs": blogs, "keyword": keyword}
    return render(request, "search.html", context)
