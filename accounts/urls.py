from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns =[
path( 'Login/', views. login_view, name='login'),
path( 'register/', views.register_view, name='register'),
path( 'logout/', views. login_view, name='logout'),
path( 'profile/', views. login_view, name='profile'),

]
