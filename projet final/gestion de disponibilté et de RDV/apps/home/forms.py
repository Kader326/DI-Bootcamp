from django import forms
from .models import liste


class liste(forms.form):
    name = forms.CharField(
        required=False, 
        min_length=3,
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Write your name here'
            })
        )
    agent_name = forms.CharField(
        required=False, 
        min_length=3,
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Write agent_name here'
            })
        )
    email = forms.EmailField(
          label="Your email", 
          help_text='Must contain at least 8 characters and a @',
          widget = forms.EmailInput(
            attrs={
                'placeholder': 'Write your email here'
            })
          ) 
    agent_grade = forms.CharField(
        required=False, 
        min_length=2,
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Write agent_grade here'
            })
        ) 
    comment = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'placeholder': 'Write your comment here'
                })
            )
 