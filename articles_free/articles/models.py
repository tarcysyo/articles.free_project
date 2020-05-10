from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField('Nome', max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']


class ArticleManager(models.Manager):
    def dashboard(self, query):
        return self.get_queryset().filter(author=query)


class Article(models.Model):
    title = models.CharField('Título', max_length=255, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='authors', verbose_name="Autor")
    abstract = models.TextField('Resumo', blank=False, null=False)
    slug = models.SlugField('Atalho', unique=True, max_length=50)
    publication_date = models.DateField('Publicado em', auto_now_add=True)
    content = models.FileField('Artigo', upload_to='articles/files', blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='articles', verbose_name="Categoria")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:detail', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
        ordering = ['publication_date']

    object = ArticleManager()