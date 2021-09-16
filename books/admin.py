from django.contrib import admin
from books.models import Publisher


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'email')
    list_filter = ['name']


admin.site.register(Publisher, PublisherAdmin)
