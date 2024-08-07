
from blog_mod.models import Category


def get_category(request):
    categories = Category.objects.all()
    return dict(categories=categories)