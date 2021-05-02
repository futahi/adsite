from django import forms
from django.contrib.auth.models import User


class UserCreationForm(forms.ModelForm):
	username = forms.CharField(label = 'Логин', max_length = 30, help_text = 'Имя пользователя не должен включать пробелы')
	email = forms.CharField(label = 'E-mail')
	first_name = forms.CharField(label = 'Имя')
	last_name = forms.CharField(label = 'Логин')
	password1 = forms.CharField(label = 'Пароль', widget = forms.PasswordInput(), min_length = 8)
	password2 = forms.CharField(label = 'Повторите пароль', widget = forms.PasswordInput(), min_length = 8)

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1','password2')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password1'] != cd['password2']:
			raise forms.ValidationError('Пароли не совпадают!')
		return cd['password2']

	def clean_username(self):
		cd = self.cleaned_data
		if User.objects.filter(username=cd['username']).exists():
			raise forms.ValidationError('Пользователь с этим логином уже существует.')
		return cd['username']
