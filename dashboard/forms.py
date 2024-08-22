from django import forms

from blog_mod.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
