from django import forms
from accounts.models import User
from accounts.authentication.customforms import SignUpForm


class RegisterForm(SignUpForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="Confirmation Password",widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('first_name','last_name','email','age','password1','password2')




