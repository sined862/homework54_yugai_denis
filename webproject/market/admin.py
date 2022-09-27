from django.contrib import admin
from market.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')
    fields = ('title', 'description')

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'category')
    list_filter = ('id', 'title', 'description', 'created_at', 'category', 'image', 'price')
    search_fields = ('id', 'title', 'description')
    fields = ('title', 'description', 'category', 'image', 'price')

admin.site.register(Product, ProductAdmin)
