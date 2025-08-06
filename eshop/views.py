from django.shortcuts import render

from eshop.models import Product


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'eshop/product_list.html',{'products':products})