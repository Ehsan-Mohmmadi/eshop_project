from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactUsModelForm
from django.views.generic.edit import FormView
    
# Create your views here.


class ContactUsView(FormView):
    template_name = 'contact_module/contact-us.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    # def get(self, request):
    #     contact_form = ContactUsModelForm()
    #     return render(request, 'contact_module/contact-us.html', {'contact_form': contact_form})
    #
    # def post(self, request):
    #     contact_form = ContactUsModelForm(request.POST)
    #     if contact_form.is_valid():
    #         contact_form.save()
    #         return redirect('home_page')
    #     return render(request, 'contact_module/contact-us.html', {'contact_form': contact_form})