from django import forms

class NewUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    fname = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lname = forms.CharField(label='Last name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    choices = [(0, 'Customer'), (1, 'Worker')]
    type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=choices)
