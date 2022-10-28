from django.contrib import admin

from .models import Publisher, Author, Series, Book

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Series)
admin.site.register(Book)