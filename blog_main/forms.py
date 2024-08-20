from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")

#  User model is default model of django which has fields like username,password,firstname,lastname,email..... 
# which we can use to create and manage users for our website

# UserCreationForm handles creating user accounts / new users. This model provides 3 fields
# username,password1(enter password), password2(confirm password) and provides validation for users

# Meta class in django is used to provide additional configurations to our model class.
# In our case it says that RegistrationForm class/model is based on user model and it should contain fields like email,uname,pass1,pass2

"""==============================================================="""
# User form is generated when we run migrate command and is only accessible in admin panel

# So if we want to see this form in the UI we use user model form called UserCreationForm which by default has 3 fields and we can add
# some extra fields present in User model to UserCreationForm model

# User - username,password,firstname,lastname,email,is_active,date_joined..............
# UserCreationForm - username,pass1,pass2 (uses User model only under the hood)