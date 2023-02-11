from django.contrib import admin
from product.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'slug']
    list_editable = ['slug']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'category', 'price', 'date_added']
    list_editable = ['category', 'price']
