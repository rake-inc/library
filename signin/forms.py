from django import forms
from passlib.hash import pbkdf2_sha256
from .models import SignUp
import re

class SignUpForm(forms.ModelForm):
	
	class Meta:
		model=SignUp
		widgets = {
		 'password' : forms.PasswordInput(attrs={
		 	'placeholder':'Password',
		 	'class' : 'form-control',
		 	}),
		 'email' : forms.EmailInput(attrs={
         'placeholder' : 'Email',
         'class' : 'form-control',
			}
			),
		 'name' : forms.TextInput(attrs={
	     'placeholder' : 'Name',
	     'class' : 'form-control',
			}
			),
		}
		fields = ['name','email','password']

	def clean_email(self):
		email = self.cleaned_data['email']
		userid,domain = email.split('@')
		if bool(re.search(r'\d',domain)):
			raise forms.ValidationError("Enter a proper email id")
		else:
			return email

	def clean_password(self):
		password = self.cleaned_data['password']
		if len(password) == 0 or len(password) <3:
			raise forms.ValidationError("Please enter your password")
		else:
			return pbkdf2_sha256.encrypt(password,rounds=120,salt_size=8)
	
	def clean_name(self):
		name = self.cleaned_data['name']
		if len(name) <3:
			raise forms.ValidationError("Enter only character")
		elif not bool(re.search(r'^[A-Za-z]',name)):
			raise forms.ValidationError("No special Characters are allowed")
		return name


class LoginForm(forms.Form):
	email = forms.CharField(
		required = True,
		label = 'Email',
		widget = forms.EmailInput(
			attrs={
			'placeholder' : 'Email',
			'class' : 'form-control',
			}
			)
		)
	password = forms.CharField(
		required = True,
		label = 'Password',
		widget = forms.PasswordInput(
			attrs={
			'placeholder' : 'Password',
			'class' : 'form-control',
			}
			)
		)
	# Validation
	def clean_email(self):
		email = self.cleaned_data['email']
		db = SignUp
		if bool(db.objects.filter(email=email)):
			return email
		else:
			raise forms.ValidationError("Incorrect Email ID")

	def clean_password(self):
		email_id = self.cleaned_data.get('email')
		pas = [y.password for y in SignUp.objects.all()]
		if len(pas) == 0:
			raise forms.ValidationError("Please Sign Up")
		em = list(str(e.email) for e in SignUp.objects.all() )
		password = pas[em.index(email_id)]
		if pbkdf2_sha256.verify(self.cleaned_data['password'],password):
			return True
		else:
			raise forms.ValidationError("Incorrect Password")
