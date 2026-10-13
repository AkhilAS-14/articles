from django import forms
from . import models


class CreateArticle(forms.ModelForm):

    class Meta:
        model = models.article
        fields = ['title', 'body', 'slug']