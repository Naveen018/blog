from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from blog_mod.models import Blog, Category, Comment
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
    # comments
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST["comment"] #This "comment" keyword is the name attribute we have given form the form in UI
        comment.save()
        return HttpResponseRedirect(request.path_info)
    # HttpResponseRedirect will take us to the same page from which we came(in this case we go back to the same page from which we commented)
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context = {"single_blog": single_blog, "comments": comments, "comment_count" : comment_count}
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
