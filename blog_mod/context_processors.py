from assignments.models import SocialLinks
from blog_mod.models import Category


def get_category(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_socialLinks(request):
    social_links = SocialLinks.objects.all()
    return dict(social_links=social_links)
