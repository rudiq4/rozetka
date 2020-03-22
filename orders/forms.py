from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address', 'email', 'postal_code', 'details']

        help_texts = {
            'postal_code': 'Необовязково',
            'email': 'Необовязково',
            'details': 'Необовязково'
        }
