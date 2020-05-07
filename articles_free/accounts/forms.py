from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nome*', 'required': 'True'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sobrenome*', 'required': 'True'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username*', 'autofocus': 'False'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email*'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha*'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmação de senha*'}))

    def save(self, commit='True'):
        user = super(RegisterForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.surname = self.cleaned_data['surname']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
