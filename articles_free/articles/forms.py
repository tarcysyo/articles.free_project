from django import forms
from articles_free.articles.models import Category, Article

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'category', 'content', 'abstract')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder':'Título do artigo*'})
        self.fields['abstract'].widget.attrs.update({'placeholder': 'Resumo ou abstract*'})