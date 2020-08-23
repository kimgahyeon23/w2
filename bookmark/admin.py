from django.contrib import admin

# Register your models here.
from bookmark.models import Bookmark


@admin.register(Bookmark)
class BookmartAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')