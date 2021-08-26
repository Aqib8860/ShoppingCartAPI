from django.contrib import admin
from . models import *

# Register your models here.


@admin.register(Cart)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'item', 'ordered']
