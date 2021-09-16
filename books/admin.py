from django.contrib import admin
from books.models import (Publisher, Book)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'email')
    list_filter = ['name']


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    list_filter = ['title']


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
