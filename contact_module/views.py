from django.shortcuts import render,redirect
from .forms import ContactForm


# Create your views here.

def contact_us(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            return redirect('home_page')

    return render(request, 'contact_module/contact-us.html', {'contact_form': contact_form})
