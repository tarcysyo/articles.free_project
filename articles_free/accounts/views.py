import re
from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from articles_free.accounts.forms import RegisterForm, EditAccountForm, EditPasswordForm
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
def edit(request):
    template_name = 'accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            context['form'] = form
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def editpassword(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = EditPasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['form'] = form
            return redirect('accounts:dashboard')
    else:
        form = EditPasswordForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def dashboard(request):
    articler = Article.objects.dashboard(request.user)
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


# @login_required
# def management(request):
#     articler = Article.objects.dashboard(request.user)
#     template_name = 'accounts/management.html'
#     context = {'articler': articler}
#     return render(request, template_name, context)
#
# @login_required
# def delete_article(slug):
#     article_to_delete=Article.objects.get(slug=slug)
#     article_to_delete.delete()
#     return redirect('accounts:management')
#
#
# @login_required
# def republication(request):
#     if request.method == "POST":
#         form = EditPublicationForm(request.POST, request.FILES)
#         if form.is_valid():
#             pub = form.save(commit=False)
#             pub.author = request.user
#             pub.publication_date = datetime.now()
#             pub.slug = urlify(pub.title) + '-' + urlify(pub.abstract)
#             form.save()
#             return redirect('accounts:management')
#     else:
#         form = EditPublicationForm()
#     context = {'form': form}
#     template_name = 'articles/edit_publication.html'
#     return render(request, template_name, context )


def urlify(string):
    string = string.lower().strip()  # remove leading, trailing whitespace
    string = string.replace("&", "and")
    string = re.sub("[^a-z0-9- ]", "", string)  # remove non-alphanumeric chars  (except dashes and spaces)
    string = re.sub("\W+", "-", string)  # replace whitespace with "-"
    string = re.sub("-{2,}", "-", string)  # remove double dahses
    return string