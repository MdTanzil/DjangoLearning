from django import forms


class Postform(forms.Form):

    title = forms.CharField()
    image = forms.FileField()
