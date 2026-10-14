from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("books:home")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("books:home")

            form.add_error(None, "Username yoki parol noto'g'ri")
    else:
        form = LoginForm()

    return render(request, 'login.html', {"form": form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect("books:home")


@login_required
def profile_view(request):
    return render(request, 'profile.html')