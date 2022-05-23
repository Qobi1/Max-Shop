from django import forms
from shop_app.models import Category


class CtgForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

