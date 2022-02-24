from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime



TIPOJURIDICODOCLIENTE = (('MEI', 'Microempreendedor Individual'),
						('PF', 'Pessoa Física'),
						('CS', 'Simples'))


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone_no = forms.CharField(max_length = 20)
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	tipo_juridico = forms.ChoiceField(widget=forms.RadioSelect, choices= TIPOJURIDICODOCLIENTE, help_text=("Informe o seu perfil."))
	CEP = forms.CharField(max_length=20)
	Data_de_cadastro_do_cliente = forms.DateField(initial=datetime.date.today)
	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'password1', 'password2', 'tipo_juridico', 'email', 'phone_no', 'CEP', 'Data_de_cadastro_do_cliente']

