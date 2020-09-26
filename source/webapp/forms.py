from django import forms
from webapp.models import Product, Review
from django.forms import widgets


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []
        widgets = {'category': forms.widgets.Select}


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['product']


