from django.urls import path

from books import views

app_name = 'book'

urlpatterns = [

path('', views. home_view, name='home'),

path('<int:pk>/',views.detail_view,name='detail'),
path('book/create/', views.book_create, name='book-create'),
path('book/update/<int:pk>/', views.book_update, name='book-update'),
path('book/delete/<int:pk>/', views.book_delete, name='book-delete'),

path('category/create/',views.category_create,name='category-create'),
path('category/update/<int:pk>/',views.category_update,name='category-update'),
path('category/delete/<int:pk>/',views.category_delete,name='category-delete'),

path('author/create/',views.author_create,name='author-create'),
path('author/update/<int:pk>/', views.author_update, name='author-update'),
path('author/delete/<int:pk>/', views.author_delete, name='author-delete'),

]