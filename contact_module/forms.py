from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(label="نام و نام خانوادگی", max_length=50,error_messages={'required': 'Enter your full name'})
    email = forms.EmailField(label="ایمیل")
    subject = forms.CharField(label="موضوع")
    message = forms.CharField(widget=forms.Textarea)
