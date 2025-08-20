from django.shortcuts import render, get_object_or_404

from eshop.models import Product


# Create your views here.
def product_list(request):
    product = Product.objects.all().order_by('price')[:5]
    return render(request, 'eshop/product_list.html',{'product':product})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug = slug)
    return render(request, 'eshop/product_detail.html', {'product':product})