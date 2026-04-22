from django.contrib import admin
from .models import Category, Post

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("name", "is_active")
    search_fields = ("name",)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ("author", "title")


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
