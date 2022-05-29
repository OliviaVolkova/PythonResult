from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms

from urls.models import UrlModel


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class UrlForm(forms.ModelForm):
    url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "input"}
    ))

    class Meta:
        model = UrlModel
        fields = ('new_url',)
        exclude = ['user',]
