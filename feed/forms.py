from django import forms


class Postform(forms.Form):

    title = forms.CharField(label='Add a title')
    image = forms.FileField(label='Upload Image')
