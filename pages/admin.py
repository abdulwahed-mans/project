from django.contrib import admin
from .models import Category, Brand, Owner, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'brand', 'owner', 'is_available')
    list_filter = ('category', 'brand', 'owner', 'is_available')
    search_fields = ('name',)
