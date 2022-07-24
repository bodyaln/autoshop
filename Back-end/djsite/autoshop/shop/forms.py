from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['shops'].empty_label = "Категория не выбрана"

    class Meta:
        model = Auto
        fields = ['firm', 'mark', 'condition', 'slug', 'content', 'price', 'year', 'distance', 'power', 'transmission', 'photo', 'fuel', 'shops'] #'__all__'
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60,'rows': 10}),
        }
    #title= forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
    #slug = forms.SlugField(max_length=255)
    #content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60,'rows': 10}))
    #is_published = forms.BooleanField(required=False, initial=True)
    #cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана")

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
