from django import forms

# Création d'un formulaire de login, sera utilisé pour le login étudiant
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)