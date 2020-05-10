from django.shortcuts import render
from .forms import Contact


# Create your views here.

def home(request):
    template_name = 'home.html'
    return render(request, template_name)


def contact(request):
    context = {}
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail()
            form = Contact()
    else:
        form = Contact()
    template_name = 'contact.html'
    context['form'] = form
    return render(request, template_name, context)
