from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book
from .forms import CreateForm, RegisterForm, LoginForm, SearchForm, CreateBookForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.core.paginator import Paginator

class dashbord(View):
    def dashboard_view(req):
        return render(req, 'dashbord.html')

class ListView(View):
    def all_info(req):
        authors = Author.objects.all()
        form = SearchForm(req.GET)
        if req.method == "GET":
            form = SearchForm(req.GET)
            if form.is_valid():
                quert = form.cleaned_data['q']
                authors = Author.objects.filter(full_name__icontains=quert)
        else:
            form = SearchForm()

        paginator = Paginator(authors, 1)
        page_num = req.GET.get('page')
        page_obj = paginator.get_page(page_num)
        context = {
            'authors': page_obj.object_list,
            'page_obj': page_obj,
            'form': form,
            'is_paginated': page_obj.has_other_pages()
            }
        return render(req, 'authors_list.html', context)

class Register_view(View):
    def register(req):
        if req.method == "POST":
            form = RegisterForm(req.POST)
            if form.is_valid():
                user = form.save()
                login(req, user)
                messages.success(req, 'Successfully registeres')
                return redirect('login_page')
        else:
            form = RegisterForm()
        return render(req, 'register.html', {'form': form})
    
class Login_View(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_view')
        return render(request, "login.html", {"form": form})  
          
class Log_Out_View(View):
    def log_out(req):
        logout(req)
        return redirect('login_page')
    
@login_required
class Create_View(View):
    def create_autho(req):
        if req.method == "POST":
            form = CreateForm(req.POST, req.FILES)
            if form.is_valid():
                form.save()
                return redirect('list_view')
        else:
            form = CreateForm()
        return render(req, 'create.html', {'form': form})

@login_required
class Update_View(View):
    def update_page(req, id):
        update = get_object_or_404(Author, id=id)
        if req.method == "POST":
            form = CreateForm(req.POST, req.FILES, instance=update)
            if form.is_valid():
                form.save()
                return redirect('list_view')
        else:
            form = CreateForm(instance=update)
        return render(req, 'update.html', {'form': form})

class Delete_View(View):
    def delete_page(req, id):
        delete = get_object_or_404(Author, id=id).delete()
        return redirect('list_view')

# FOR ALL BOOKS 
"""
Book List

"""
@login_required
class Book_List_view(View):
    def all_books(request):
        books = Book.objects.all()
        return render(request, 'books.html', {'books': books})
@login_required
class Book_Create(View):
    def create_books(request):
        if request.method == "POST":
            form = CreateBookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('books')
        else:
            form = CreateBookForm()
        return render(request, 'book_c.html', {'form': form})
    
class Update_Book(View):
    def update_books(req, id):
        update = get_object_or_404(Book, id=id)
        if req.method == "POST":
            form = CreateBookForm(req.POST, req.FILES, instance=update)
            if form.is_valid():
                form.save()
                return redirect('books')
        else:
            form = CreateBookForm(instance=update)
        return render(req, 'book_update.html', {'form': form})
    
class Delete_Books(View):
    def delete_b(req, id):
        get_object_or_404(Book, id=id).delete()
        return redirect('books')