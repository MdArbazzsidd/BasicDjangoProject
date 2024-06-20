from django import forms

from .models import Tweet

class TweetFrom(forms.ModelForm):
    class Meta:
        model=Tweet
        fields = ['text','photos']