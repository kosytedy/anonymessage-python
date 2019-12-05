from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control mb-1',
                'placeholder': 'Enter your message here..',
                'cols': 30,
                'rows': 5
            }
        )
    )

    class Meta:
        model = Message
        fields = ('message',)