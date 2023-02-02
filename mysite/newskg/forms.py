from django import forms
from .models import Purpose

class LangForm (forms.Form):
    title = forms.CharField (max_length=150)
    content = forms.CharField ()
    is_published = forms.BooleanField ()
    purpose = forms.ModelChoiceField (queryset=Purpose.objects.all ())