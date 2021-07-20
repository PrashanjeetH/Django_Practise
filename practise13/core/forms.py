from django import forms
from core.models import ProfileModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('__all__')