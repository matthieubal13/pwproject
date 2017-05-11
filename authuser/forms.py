from django import forms

class ConnexionForm(forms.Form):
    username = forms.CharField(label="User name", max_length=30,
    widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label="Password",
    widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
