from django import forms
from .models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'first_name': 'First name',
        }
        error_messages = {
            'first_name':{
                'required': 'You cannot move forward without first name!'
            },
        }
        help_texts = {}