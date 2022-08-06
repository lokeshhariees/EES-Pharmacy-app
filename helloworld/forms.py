from django import forms
from django.forms import ModelForm

from helloworld.models import bill,product,bill_products

class billform(forms.ModelForm):
    class Meta:
        model=bill
        fields=['customer_name']


class billproductform(forms.ModelForm):
    class Meta:
        model=bill_products
        fields=['bill_product','quantity']