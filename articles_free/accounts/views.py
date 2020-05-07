from django.conf import settings
from django.shortcuts import render, redirect
from articles_free.accounts.forms import RegisterForm

# Create your views here.


def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, template_name, context)