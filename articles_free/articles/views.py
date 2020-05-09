from datetime import datetime

from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from articles_free.articles.forms import PublicationForm
from articles_free.articles.models import Article


# Create your views here.

def index(request):
    articles = Article.objects.all()
    template_name = 'articles/index.html'
    context = {'articles': articles}
    return render(request, template_name, context)


def detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    template_name = 'articles/detail.html'
    context = {'article': article}
    return render(request, template_name, context)


def publication(request):
    template_name = 'articles/publication.html'
    context = {}
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            pub = form.save(commit=False)
            pub.author = request.user
            pub.publication_date = datetime.now()
            pub.slug = pub.title.lower().strip().replace(' ','-')+'-'+pub.abstract.lower().strip().replace(' ','-')
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = PublicationForm()
    context['form'] = form
    return render(request, template_name, context)


# def publication(request):
#     template_name = 'articles/publication.html'
#     if request.method == 'POST':
#         form = PublicationForm(request.POST)
#         if form.is_valid():
#             #form.save()
#             return redirect(settings.LOGIN_URL)
#     else:
#         form = PublicationForm()
#     context = {'form': form}
#     return render(request, template_name, context)
