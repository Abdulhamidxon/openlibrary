from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import CategoryModelForm
from books.forms import BookModelForm, AuthorModelForm
from books.models import BookModel, AuthorModel, CategoryModel


# FBV -> Function Based View
# CBV -> Class Based View


def home_view(request):
    book = BookModel.objects.all()
    category = CategoryModel.objects.all()
    author = AuthorModel.objects.all()

    context = {
        'books':book,
        'category':category,
        'authors':author,
    }

    return render(request,'index.html',context)

def detail_view(request, pk):
    book = BookModel.objects.get(pk=pk)

    context = {
        'book': book,
    }

    return render(request,'book_detail.html',context)

# Category
def category_create(request) :
    if request.method == "POST":
        form = CategoryModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book:home')

    else:
        form = CategoryModelForm()

    context ={
        'form':form
    }

    return render(request,'category_create.html', context)


def category_update(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk)
    if request.method == "POST":
        form = CategoryModelForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect('book:home')

    else:

        form = CategoryModelForm(instance=category)

    context = {
        'form': form,
        'category': category,
    }

    return render(request,'category_update.html', context)


def category_delete(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk)

    if request.method == "POST":
        category.delete()
        return redirect('book:home')

    context = {
        'category': category,
    }

    return render(request,'category_delete.html', context)


# book
def book_update(request, pk):
    book = get_object_or_404(BookModel, pk=pk)
    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()
            return redirect('book:home')

    else:

        form = BookModelForm(instance=book)

    author = AuthorModel.objects.all()
    category = CategoryModel.objects.all()

    context = {
        'book': book,
        'form': form,
        'author': author,
        'category': category,
    }

    return render(request,'book_update.html', context)

def book_delete(request, pk):
    book = get_object_or_404(BookModel, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect('book:home')

    context = {
        'book': book,
    }

    return render(request,'book_delete.html', context)


def book_create(request):
    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        return redirect('book:home')

    else:
        form = BookModelForm()

    author = AuthorModel.objects.all()
    category = CategoryModel.objects.all()

    context = {
        'form': form,
        'authors': author,
        'category': category,
    }

    return render(request,'book_create.html', context)


# author
def author_update(request, pk):
    author = get_object_or_404(AuthorModel, pk=pk)
    if request.method == "POST":
        form = AuthorModelForm(request.POST, instance=author)

        if form.is_valid():
            author.save()
            return redirect('book:home')

    else:

        form = AuthorModelForm(instance=author)

    context = {
        'form': form,
        'authors': author,
    }

    return render(request,'author_update.html', context)





def author_delete(request, pk):
    author = get_object_or_404(AuthorModel, pk=pk)
    if request.method == "POST":
        form = AuthorModelForm(request.POST, instance=author)

        if request.method == "POST":
            author.delete()
        return redirect('book:home')

    else:

        form = AuthorModelForm(instance=author)

    context = {
        'form': form,
        'author': author,
    }

    return render(request,'author_delete.html', context)


def author_create(request):
    if request.method == "POST":
        form = AuthorModelForm(request. POST)

        if form.is_valid():
            form.save()
            return redirect("book:home")

    else:

        form = AuthorModelForm()

    context = {
        'form':form,
    }

    return render(request,'author_create.html', context)