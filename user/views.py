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
	
	return render(request, 'user/index.html', {'title':'home'})

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
            """subject, from_email, to = 'Bem vindo', 'efidelity01@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Sua conta foi criada! Agora você pode fazer Login')"""
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'registre'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Bem vindo {username}!')
            return redirect('index')
        else:
            messages.info(request, f'Usuário não identificado, tente novamente')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})


########## prediction ######################################

def prediction(request):
	
	return render(request, 'user/prediction.html', {'title':'prediction'})

########## biometric ######################################

def biometric(request):
	
	return render(request, 'user/biometric.html', {'title':'biometric'})


########### diagnostic #####################################

def diagnostic(request):
	
	return render(request, 'user/diagnostic.html', {'title':'diagnostic'})

########### database #######################################

def database(request):
	
	return render(request, 'user/database.html', {'title':'database'})

########### Veterinary #####################################

def veterinary(request):
	
	return render(request, 'user/veterinary.html', {'title':'veterinary'})

########### Índices ##########################################

def indices(request):
	
	return render(request, 'user/indices.html', {'title':'indices'})

