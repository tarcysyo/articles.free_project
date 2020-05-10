from django import forms
from django.conf import settings
from articles_free.core.email import send_email_template

class Contact(forms.Form):
    name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'placeholder':'Nome*'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder':'Email*', 'type':'email'}))
    subject = forms.CharField(max_length=200, required=False, widget= forms.TextInput(attrs={'placeholder':'Assunto'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Mensagem*'}))

    def send_mail(self):
        subject = '%(subject)s'
        context = {'subject': self.cleaned_data['subject'], 'name': self.cleaned_data['name'], 'email': self.cleaned_data['email'], 'message': self.cleaned_data['message']}
        template_name = "contact_email.html"
        subject = subject % context
        send_email_template(subject, template_name,context,[settings.CONTACT_EMAIL])