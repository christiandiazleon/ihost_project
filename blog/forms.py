from django import forms
from blog.models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('author', 'title', 'text', 'image')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {
            'name':forms.TextInput(attrs={'class':'textinputclass'}),
            'body': forms.Textarea(attrs={'class':'editable medium-editor-textarea '})

        }
