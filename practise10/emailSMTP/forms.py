from django import forms
from .models import SmtpMailModel


class smtpMailForm(forms.ModelForm):
    class Meta:
        model = SmtpMailModel
        fields = ('sender', 'receiver', 'subject', 'body')
