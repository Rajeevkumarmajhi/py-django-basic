from django.contrib import admin
from .models import Category, SubCategory, Product

# Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# SubCategory admin
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')  # category FK shown here

# Product admin (already working)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'sub_category', 'price', 'quantity')



admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)