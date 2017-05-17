from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label="Search", max_length=200, required=False,
    widget=forms.TextInput(attrs={'class' : 'form-control'}))
    phenotypes = forms.CharField(label="Phenotypes", max_length=200,
    required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
