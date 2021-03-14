from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=256)
    token = forms.CharField(label='Token', max_length=256)