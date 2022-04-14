from django import forms

class NewUserForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='First name', max_length=100)
    password = forms.PasswordInput()
