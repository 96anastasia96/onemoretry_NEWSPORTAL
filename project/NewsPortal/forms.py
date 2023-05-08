from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'categories',
            'rating',
            'type',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Заголовок не может быть идентичен тексту."
            )
        return cleaned_data


#class SubcribersForm(forms.ModelForm):
#    class Meta:
#        model = Subscribers
#        fields = ['email', 'category']