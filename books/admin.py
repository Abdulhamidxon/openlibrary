from django.contrib import admin

from books.models import CategoryModel, AuthorModel, BookModel


admin.site.register(CategoryModel)


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price')
    search_fields = ('title', 'price')
    list_filter = ('price', 'pages', 'author', 'category')
