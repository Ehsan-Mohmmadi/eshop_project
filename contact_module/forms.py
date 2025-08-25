from django import forms
from contact_module.models import ContactUs


class ContactForm(forms.Form):
    full_name = forms.CharField(
        label="نام و نام خانوادگی",
        max_length=50,
        error_messages={'required': 'نام کامل خود را وارد نمایید'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}),
    )
    email = forms.EmailField(
        label="ایمیل",
        error_messages={'required': 'لطفا ایمیل خود را وارد نمایید'},
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل', })
    )
    title = forms.CharField(
        label="موضوع",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پیام شما', 'id': 'message'})
    )


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'title', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'موضوع'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'متن پیام', 'id': 'message'})
        }
