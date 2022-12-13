from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from  .models import PersonDetail

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	nome = forms.CharField(max_length = 20)
	sobrenome = forms.CharField(max_length = 20)
	class Meta:
		model = User
		fields = ['nome','sobrenome','username', 'email', 'password1', 'password2']


class PersonDetailForm(forms.ModelForm):

    class Meta:
        model = PersonDetail
        fields = ('user','matriz','reprodutor','parto','data_de_nascimento','habilidade_materna')
        exclude = ['user']