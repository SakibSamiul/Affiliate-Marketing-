from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.filter(id=id).first()
    if product is None:
        return HttpResponse('Product not found.')

    return render(request, 'product_details.html', {'product':product})