from django import forms

class NewUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    fname = forms.CharField(label='First name', max_length=100)
    lname = forms.CharField(label='Last name', max_length=100)
    choices = [(0, 'Customer'), (1, 'Worker')]
    type = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)
