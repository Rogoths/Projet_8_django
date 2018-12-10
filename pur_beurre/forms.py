from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=forms.PasswordInput)#widget adapt html code for the type of used form


class SignInForm(forms.Form):
	username = forms.CharField(max_length=30)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
confirm_password = forms.CharField(widget=forms.PasswordInput)
