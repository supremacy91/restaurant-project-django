from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Cook


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search...",
            }
        ),
    )


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )
