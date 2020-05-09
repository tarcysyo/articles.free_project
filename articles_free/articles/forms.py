from django import forms
from articles_free.articles.models import Category, Article


# class PublicationForm(forms.Form):
#     title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Título do Artigo*'}))
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'placeholder': 'Autor*'}))
#     content = forms.FileField()
#     abstract = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Resumo ou Abstract'}))

class PublicationForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'category', 'content', 'abstract')