from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request,'home_module/index_page.html')

def site_header_partial(request):
    return render(request,'shared/site_header_partial.html')

def site_footer_partial(request):
    return render(request,'shared/site_footer_partial.html')