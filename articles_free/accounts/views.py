import re
from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from articles_free.accounts.forms import RegisterForm
from articles_free.articles.forms import PublicationForm
from articles_free.articles.models import Article


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


@login_required
def dashboard(request):
    articler = Article.object.dashboard(request.user)
    template_name = 'accounts/dashboard.html'
    context = {'articler': articler}
    return render(request, template_name, context)


@login_required
def publication(request):
    template_name = 'articles/publication.html'
    context = {}
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            pub = form.save(commit=False)
            pub.author = request.user
            pub.publication_date = datetime.now()
            pub.slug = urlify(pub.title) + '-' + urlify(pub.abstract)
            form.save()
            return redirect('accounts:dashboard')
    else:
        form = PublicationForm()
    context['form'] = form
    return render(request, template_name, context)


def urlify(string):
    string = string.lower().strip()  # remove leading, trailing whitespace
    string = string.replace("&", "and")
    string = re.sub("[^a-z0-9- ]", "", string)  # remove non-alphanumeric chars  (except dashes and spaces)
    string = re.sub("\W+", "-", string)  # replace whitespace with "-"
    string = re.sub("-{2,}", "-", string)  # remove double dahses
    return string