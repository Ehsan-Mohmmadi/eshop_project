from django.shortcuts import render, redirect
from .forms import ContactForm, ContactUsModelForm
from .models import ContactUs
# Create your views here.

def contact_us(request):
    #contact_form = ContactForm()
    contact_form = ContactUsModelForm()
    #contact = ContactUsModelForm(request.POST)

    if request.method == "POST":
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            # contact = ContactUs(full_name=contact_form.cleaned_data.get('full_name'),
            #                     email=contact_form.cleaned_data.get('email'),
            #                     message=contact_form.cleaned_data.get('message'),
            #                     title=contact_form.cleaned_data.get('title'),
            #                     is_read=False
            #                     )
            # print(contact_form.cleaned_data)
            # contact.save()
            contact_form.save()
            return redirect('home_page')
    return render(request, 'contact_module/contact-us.html', {'contact_form': contact_form})
