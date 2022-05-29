from django.contrib.auth.forms import UserCreationForm
from django import forms

from urls.models import UrlModel, User


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class UrlForm(forms.ModelForm):
    url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "input"}
    ))

    class Meta:
        model = UrlModel
        fields = ('url',)
        exclude = ['user',]
