from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Your "name"', max_length=256)
    token = forms.CharField(label='Your token', max_length=256)