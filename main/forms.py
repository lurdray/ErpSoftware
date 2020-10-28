from django.contrib.auth.models import User
from django import forms
from department.models import Department


class UserForm(forms.ModelForm):
	password1 = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields = ("username", "password1", "password2")



class SignUpForm(forms.ModelForm):

	class Meta():
		model = Department
		fields = ("name", "head")
		

	
class LoginForm(forms.Form):
	username = forms.CharField(label="username")
	password = forms.CharField(label="password", widget=forms.PasswordInput())
	account_type = forms.CharField(label="account type")


