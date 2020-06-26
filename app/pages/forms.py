from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput
from .models import Feedback

class FeedBackForm(forms.ModelForm):
    """Class form for a contact page"""
    name = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя',
                'data-error': 'Так как же вас зовут?',
                               }
        )
    )
    email = forms.CharField(
        label=False,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта',
                'data-error': 'Забыли указать почту',
            }
        )
    )
    subject = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Тема',
                'data-error': 'Забыли указать тему',
            }
        )
    )
    content = forms.CharField(
        label=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 11,
                'placeholder': 'Слушаю вас...',
                'data-error': 'Забыли написать, в чем суть проблемы',
            }
        )
    )
    captcha = CaptchaField()

    error_messages = {
        "password_mismatch": "Пароли не совпадают.",
        "duplicate_username": "Такой пользователь уже есть",
        'password_too_common': 'Часто используемый пароль',
        'unique_together': 'Уникальные пароли',
        'password_entirely_numeric': 'Пароль не должен состоять только из цифр',
        'invalid': 'Не разгадали капчу'
    }

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'content')


