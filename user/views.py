from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse
from django.conf import settings
import os
import requests
import time
from django.http import JsonResponse


#from tabulate import tabulate

#--------------------------------------------- Usuário --------------------------------------------------------

#################### index#######################################
def index(request):
	
	return render(request, 'user/index.html', {'title':'E-Fidelity| O cartão fidelidade digital.'})


########### register here #####################################
def register(request):
	if request.method == 'POST':
		
		form = UserRegisterForm(request.POST)
		
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system ####################################
			htmly = get_template('user/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'Bem vindo', 'your_email@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			##################################################################
			messages.success(request, f'Sua conta foi criada! Agora você pode fazer Login.')
			#send_mail(subject, message, from_email, to_list, fail_silently=Tre)
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form, 'title':'E-Fidelity| Cadastro'})

################ login forms###################################################
def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		first_name = request.POST.get('first_name')
		tipo_juridico = request.POST.get('tipo_juridico', False)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password, tipo_juridico = tipo_juridico, first_name = first_name)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' Bem vindo {username}!')
			return redirect('index')
		else:
			messages.info(request, f'Usuário não identificado, tente novamente.')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'E-Fidelity| Login'})

########### beneficios ######################################

def beneficios(request):
	
	return render(request, 'user/beneficios.html', {'title':'E-Fidelity| O cartão fidelidade digital.'})


########### seções #####################################

images=[]

def getFiles(path):
	for file in os.listdir(path):
		if file.endswith(".png"):
			images.append(os.path.join(path, file))
            
filesPath = r".\user\static\images\fidelity"

getFiles(filesPath)

def section(request, num):
	if 1 <= num <= 11:
		with open(images[num-1], "rb") as f:
			return HttpResponse(f.read(), content_type="image/png")    
	else:
		raise Http404("No such section")

#--------------------------------------------- Logista --------------------------------------------------------

########### historico ######################################

def historico(request):
	
	return render(request, 'user/historico.html', {'title':'E-Fidelity| O cartão fidelidade digital.'})

########### clientes #######################################

def clientes(request):
	
	return render(request, 'user/clientes.html', {'title':'E-Fidelity| O cartão fidelidade digital.'})

########### publication #####################################

def posts(request):

    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Poste {i}, Desconto de 10% em compras acima de 100 R$.")

    # Artificially delay speed of response
    time.sleep(1)

    # Return list of posts
    return JsonResponse({
        "posts": data
    })


def publication(request):
	
	return render(request, 'user/publication.html', {'title':'E-Fidelity| O cartão fidelidade digital.'})

########### card ############################################

def card(request):
	
	return render(request, 'user/card.html', {'title':'E-Fidelity| O cartão fidelidade digital.'})

