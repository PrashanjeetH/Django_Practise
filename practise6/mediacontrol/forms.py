from django import forms
from .models import Playlist

#Define your form defniations here

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['title','genre','singer','mp3']
