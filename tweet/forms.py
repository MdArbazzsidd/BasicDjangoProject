from django import forms

from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields = ['text','photo']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=25, label='Search')