from django import forms

from blog_mod.models import Blog, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class AddUserForm(UserCreationForm):
    # Just like we have used in user registration form ---> UCF gives username,pass1,pass2 fields we add extra fields to this from User model and render this form in UI
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )
        # Even though we haven't mentioned any pass1 or pass2 in our fields list, it will still render in UI form bacause
        # when we inherit UserCreationForm it will mandatorily show pass1 and pass2 fields in UI
        
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        ) # Now we haven't used UserCreationForm here hence edit form will not show pass1 and pass2 fields in UI
