from django.shortcuts import render

from eshop.models import Product


# Create your views here.
def product_list(request):
    return render(request, 'eshop/product_list.html')