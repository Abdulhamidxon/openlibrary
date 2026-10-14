from django import forms

from books.models import CategoryModel, AuthorModel, BookModel

# ModelForm & Form
class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['name' ]

class AuthorModelForm(forms. ModelForm) :
    class Meta:
        model = AuthorModel
        fields = ['first_name', 'last_name', 'nickname' ]
        extra_kwargs = {
            "nickname": {'allow_null': True, 'required' : False},
        }

class BookModelForm(forms.ModelForm) :
    class Meta:
        model = BookModel
        fields = "__all__"
