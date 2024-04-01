from django import forms
from .models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        error_messages = {
            'first_name':{
                'required': 'First name is required!'
            },
            'last_name':{
                'required': 'Last name is required!'
            },
            'email':{
                'required':'Email is required!'
            },
            'option':{
                'option':'Option is required!'
            }
        }
