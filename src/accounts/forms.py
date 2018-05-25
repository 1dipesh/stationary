from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class GuestForm(forms.Form):
	email = forms.EmailField()

class LoginForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class": "form-control",
			"placeholder": "username",
			"id": "username"
			}
			)

		)
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={
		"class": "form-control",
		"placeholder": "password"
		}))


class RegisterForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
			"placeholder": "Your full name",
			"class": "form-control",
			"id": "form_full_name"
			}
			)
		)
	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={

			"placeholder": "Your Email",
			"class": "form-control"
			}
			)
		)
	password = forms.CharField(widget=forms.PasswordInput(
			attrs={
			"placeholder": "Password",
			"class": "form-control"
			}
			)
		)
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
			attrs={
			"placeholder": "Confirm password",
			"class": "form-control"
			}
		))

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("username is taken")
		return username	


	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is taken")
		return email		

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("Passwords dont match")
		return data	