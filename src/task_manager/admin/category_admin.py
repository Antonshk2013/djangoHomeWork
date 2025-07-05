from django.contrib import admin
from src.task_manager.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']



admin.site.register(Category, CategoryAdmin)