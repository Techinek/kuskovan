from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


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


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Эл. почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()


    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User._default_manager.get(username=username)
            # if the user exists, then let's raise an error message
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],  # user my customized error message
                code='duplicate_username',  # set the error message key
            )
        except User.DoesNotExist:
            return username  # great, this user does not exist so we can continue the registration process

    error_messages = {
        "password_mismatch": "Пароли не совпадают.",
        "duplicate_username": "Такой пользователь уже есть",
        'password_too_common': 'Часто используемый пароль',
        'unique_together': 'Уникальные пароли',
        'password_entirely_numeric': 'Пароль не должен состоять только из цифр',
        'invalid': 'Не разгадали капчу'
    }

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    error_messages = {
        "invalid_login": "Логин и пароль не совпадают. Возможно, включен CAPSLOCK!",
    }