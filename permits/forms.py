from django import forms


class SearchCarForm(forms.Form):
    number = forms.CharField(required=True)
