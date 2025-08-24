from importlib.metadata import requires

from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        label="نام و نام خانوادگی",
        max_length=50,
        error_messages={'required': 'نام کامل خود را وارد نمایید'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}),
    )
    email = forms.EmailField(
        label="ایمیل",
        error_messages={'required':'لطفا ایمیل خود را وارد نمایید'},
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل', })
    )
    subject = forms.CharField(
        label="موضوع",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پیام شما','id':'message'})
    )
