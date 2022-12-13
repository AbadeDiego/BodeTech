from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse
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
from .models import *

from django.shortcuts import render
from django.views.generic import View
from .forms import PersonDetailForm

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
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
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


########### Índices ##########################################

class Indices(View):
    context = {}

    def get(self,request):
        forml = PersonDetailForm()
        self.context['forml'] = forml 
        self.context['detail'] = PersonDetail.objects.filter(user= request.user)
        return render(request,'user/indices.html',self.context)

    def post(self,request):
        forml = PersonDetailForm(request.POST)
        if forml.is_valid():
            forml.save()

        self.context['forml'] = forml
        self.context['detail'] = PersonDetail.objects.filter(user= request.user)
        return render(request, 'user/indices.html', self.context)

@csrf_exempt
class Home(View):
    context = {}

    def get(self,request):
        forml = PersonDetailForm()
        self.context['forml'] = forml
        self.context['detail'] = PersonDetail.objects.all()
        return render(request,'user/home.html',self.context)

    def post(self,request):
        forml = PersonDetailForm(request.POST)
        if forml.is_valid():
            forml.save()

        self.context['forml'] = forml
        self.context['detail'] = PersonDetail.objects.filter(user= request.user)
        request.user.new_spending.add(forml.save()) 

        return render(request, 'user/home.html', self.context)


    #https://vinaykumarmaurya30.medium.com/saving-data-using-django-model-form-7ec9d8471ccf
    #https://github.com/CalebCurry/django-modelform/blob/main/djangouploads/views.py
    #http://www.learningaboutelectronics.com/Articles/How-to-save-data-from-a-form-to-a-database-table-in-Django.php