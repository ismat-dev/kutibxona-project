from django.contrib import admin
from .models import Author, Book
from unfold.admin import ModelAdmin

@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    list_display=['full_name', 'image', 'country']

@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display=['title', 'price', 'author', 'image']