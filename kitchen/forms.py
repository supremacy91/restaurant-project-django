from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Cook, Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = (
            "name",
            "description",
            "price",
            "dish_type",
            "cooks",
        )
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter dish name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter dish description",
                    "rows": 4,
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter dish price",
                    "step": "0.01",
                }
            ),
            "dish_type": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "cooks": forms.SelectMultiple(
                attrs={
                    "class": "form-control",
                    "size": 6,
                }
            ),
        }


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


