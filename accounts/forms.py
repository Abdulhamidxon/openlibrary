from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import UserModel
from books.models import CategoryModel, AuthorModel

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


# Form
class CategoryModelForm(forms. ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['name' ]

class AuthorModelForm(forms.ModelForm) :
    class Meta:
        model = AuthorModel
        fields = ['first_name', 'last_name', 'nickname' ]
        extra_kwargs = {
            "nickname": {'allow_null': True, 'required' : False},
        }


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']