from django.shortcuts import render, get_object_or_404
from articles_free.articles.models import Article

# Create your views here.

def index(request):
    articles = Article.object.all()
    template_name = 'articles/index.html'
    context = {'articles': articles}
    return render(request, template_name, context)


def detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    template_name = 'articles/detail.html'
    context = {'article': article}
    return render(request, template_name, context)