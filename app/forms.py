from django import forms 
from django.contrib.auth.models import User


class UserSignUpForm(forms.Form):
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username...'}))
	email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email...'}))
	password1 = forms.CharField(label='Password', max_length=150, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password...'}))
	password2 = forms.CharField(label='Password(Confirm)', max_length=150, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password...'}))

	def clean_username(self):
		username = self.cleaned_data['username']
		user = User.objects.filter(username=username)

		invalid_chars = ['-', '+', '=', '@', '!', '?', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '.', ',', '/', '\\', '|', '`', ':', ';']
		for char in invalid_chars:
			if char in username:
				raise ValidationError('Your username have invalid characters..!')

		if user.exists():
			raise ValidationError('This username already exists..!')
		return username

	def clean(self):
		cd = self.cleaned_data
		# username = cd.get('username')
		p1 = cd.get('password1')
		p2 = cd.get('password2')

		# if p1 in username or p2 in username:
		# 	raise ValidationError('You can not using the username in the password..!')

		if p1 and p2 and p1 != p2:
			raise ValidationError('The passwords do not match..!')

		if len(p1) < 8 or len(p2) < 8:
			raise ValidationError('The lenght of passwords must 8 or longer characters..!')


class UserSignInForm(forms.Form):
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username...'}))
	password = forms.CharField(label='Password', max_length=150, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password...'}))


class UserUpdateForm(forms.Form):
	email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email...'}))
	