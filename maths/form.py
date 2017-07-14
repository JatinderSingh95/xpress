from django import forms

class userform(forms.Form):
    field = forms.CharField(label='numone', max_length=80)