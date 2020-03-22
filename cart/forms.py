from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 5)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Кількість')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    # def __init__(self, *args, **kwargs):
    #     super(CartAddProductForm, self).__init__(*args, **kwargs)
    #     self.fields['quantity'].widget.attrs.update({'class': 'default-select'})
    #     self.fields['update'].widget.attrs.update({'class': 'default-select'})
