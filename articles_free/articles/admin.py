from django.contrib import admin
from articles_free.articles.models import Category, Article, Author


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publication_date', 'category']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', 'abstract')}

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)
