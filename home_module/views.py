from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
    

# Create your views here.

# class HomePageView(View):
#     def get(self, request):
#         return render(request, 'home_module/index_page.html')

class HomePageView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'This is data'


def site_header_partial(request):
    return render(request, 'shared/site_header_partial.html')


def site_footer_partial(request):
    return render(request, 'shared/site_footer_partial.html')
