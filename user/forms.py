from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	nome = forms.CharField(max_length = 20)
	sobrenome = forms.CharField(max_length = 20)
	Data_de_cadastro = forms.DateField(initial=datetime.date.today)
	class Meta:
		model = User
		fields = ['nome','sobrenome','username', 'password1', 'password2', 'email']

