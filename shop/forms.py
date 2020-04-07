from django import forms
from .models import CustomerQuestions


class CustomerQuestionForm(forms.ModelForm):
    class Meta:
        model = CustomerQuestions
        fields = '__all__'

        # help_texts = {
        #     'postal_code': 'Необовязково',
        #     'email': 'Необовязково',
        #     'details': 'Необовязково'
        # }
