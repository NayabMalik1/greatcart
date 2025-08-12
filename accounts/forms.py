from django import forms
from .models import Account
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput({
        'placeholder': 'Enter Password',
         'class': 'form-control'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput({
        'placeholder': 'Confirm Password'}))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']


    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Enter First Name',
            'class': 'form-control'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Enter Last Name',
            'class': 'form-control'
        })
        self.fields['phone_number'].widget.attrs.update({
            'placeholder': 'Enter Phone Number',
            'class': 'form-control'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter Email',
            'class': 'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter Password',
            'class': 'form-control'
        })
        self.fields['confirm_password'].widget.attrs.update({
            'placeholder': 'Confirm Password',
            'class': 'form-control'
        })

  

 


    