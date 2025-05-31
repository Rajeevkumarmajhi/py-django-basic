from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.select_related('category', 'sub_category').all()
    return render(request, 'product/product_list.html', {'products': products})
