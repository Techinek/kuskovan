from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """Class for blog comment form"""
    content = forms.CharField(
        widget=forms.Textarea(attrs={
                'class': 'form-control w-100',
                'name': "comment",
                'id': "comment",
                'cols': "30",
                'rows': "9",
                'placeholder': "Ваш комментарий"
            }),
        label=False)

    class Meta:
        model = Comment
        fields = ['content', ]