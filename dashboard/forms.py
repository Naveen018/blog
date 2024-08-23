from django import forms

from blog_mod.models import Blog, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            "title",
            "category",
            "featured_image",
            "short_description",
            "blog_body",
            "status",
            "is_featured",
        )
        # We should not give __all__ fields here because the posts will be added by editor/author, so when we give all fields
        # it will give option to select author which shouldn't be the case. The editor who is adding post should be selected as
        # author by default

        # Also slug field should be automatically generated based on title we give
