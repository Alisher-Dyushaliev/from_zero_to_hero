from django import forms
# from .models import Purpose
from .models import Newskg
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class LangForm (forms.ModelForm):
    captcha = CaptchaField ()

    class Meta:
        model = Newskg
        # fields = '__all__'
        fields = ['title', 'content', 'info', 'is_published', 'purpose']
        widgets = {
            'title': forms.TextInput (attrs={'class': 'form-control'}),
            'content': forms.TextInput (attrs={'class': 'form-control'}),
            'info': forms.Textarea (attrs={'class': 'form-control', 'rows': 5}),
            'purpose': forms.Select (attrs={'class': 'form-control'}),
        }

    def clean_title (self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("Don't start with a number")
        return title

    def clean_content (self):
        content = self.cleaned_data['content']
        if re.match(r'\d', content):
            raise ValidationError("Don't start with a numbers")
        return content

# class LangForm (forms.Form):
    # title = forms.CharField (max_length=150, label='Language', widget=forms.TextInput (attrs={'class': 'form-control'}))
    # content = forms.CharField (label='Framework', widget=forms.TextInput (attrs={'class': 'form-control'}))
    # info = forms.CharField (required=False, label='Information', widget=forms.Textarea (attrs={
                                                                                    # 'class': 'form-control',
                                                                                    # 'rows': 5
                                          # }))
    # is_published = forms.BooleanField (initial=True, label='Publication')
    # purpose = forms.ModelChoiceField (queryset=Purpose.objects.all (), empty_label='Select purpose', label='Purpose',
                                                                    # widget=forms.Select (attrs={'class': 'form-control'})
                                                                # )

class UserRegisterForm (UserCreationForm):
    username = forms.CharField (label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField (label='Email', help_text='Required symbol-@', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField (label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField (label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField ()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput (attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput (attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput (attrs={'class': 'form-control', 'rows': 5}),
        #     'password2': forms.PasswordInput (attrs={'class': 'form-control'}),
        # }

class UserLoginForm (AuthenticationForm):
    username = forms.CharField (label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField (label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField ()


class EmailForm (forms.Form):
    subject = forms.CharField (label='Theme', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField (label='Text', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}))
    captcha = CaptchaField ()