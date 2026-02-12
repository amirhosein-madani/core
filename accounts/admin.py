from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("username" , "email" , "phone_number" , "is_superuser")
    search_fields = ("email", "username", "phone_number")

admin.site.register(User , UserAdmin)