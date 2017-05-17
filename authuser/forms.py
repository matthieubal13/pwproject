from django import forms

class ConnectionForm(forms.Form):
    """This form is made for authentication of user.
    It contains an username field and a password field.
    """
    username = forms.CharField(label="User name", max_length=30,
    widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label="Password",
    widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
