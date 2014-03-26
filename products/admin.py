from django.contrib import admin
from products.models import Product
from products.models import Category

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['description']

class CategoryAdmin(admin.ModelAdmin):
     list_filter = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)