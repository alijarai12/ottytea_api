from django.contrib import admin
from .models import Cartitem

@admin.register(Cartitem)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','customer', 'tea', 'quantity']
    