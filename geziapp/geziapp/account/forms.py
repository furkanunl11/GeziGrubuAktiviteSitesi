from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class":"form-control form-control-user","placeholder":"Email Adresinizi Giriniz..."}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Şifrenizi Giriniz..."}))
    remember_me = forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={"class":"custom-control-input"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error("email","Email ile kayıtlı bir kullanıcı yok.")

        return email