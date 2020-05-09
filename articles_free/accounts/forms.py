from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nome*', 'required': 'True'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sobrenome*', 'required': 'True'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username*', 'autofocus': 'False'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email*'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha*'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmação de senha*'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe um usuário com este e-mail.')
        return email

    def save(self, commit='True'):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
