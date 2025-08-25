from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView
from eshop.models import Product


#Create your views here.
class ProductListView(ListView):
    template_name = 'eshop/product_list.html'
    model = Product
    context_object_name = 'products'

# class ProductListView(TemplateView):
#     template_name = 'eshop/product_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductListView,self).get_context_data()
#         context['product_li'] = Product.objects.all()
#         return context

# def product_list(request):
#     product = Product.objects.all()
#     return render(request, 'eshop/product_list.html',{'product_li':product})

class ProductDetailView(TemplateView):
    template_name = 'eshop/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView,self).get_context_data()
        slug = self.kwargs['slug']
        product = get_object_or_404(Product, slug=slug)
        context['product'] = product
        return context

# def product_detail(request, slug):
#
#     return render(request, 'eshop/product_detail.html', {'product':product})