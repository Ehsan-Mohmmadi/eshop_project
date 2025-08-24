from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactUs
# Create your views here.

def contact_us(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = ContactUs(name=contact_form.cleaned_data.get('full_name'),
                                email=contact_form.cleaned_data.get('email'),
                                message=contact_form.cleaned_data.get('message'),
                                title=contact_form.cleaned_data.get('subject'),
                                is_read=False
                                )
            print(contact_form.cleaned_data)
            contact.save()
            return redirect('home_page')

    return render(request, 'contact_module/contact-us.html', {'contact_form': contact_form})
