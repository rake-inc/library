from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
from . import forms
from django.core.cache import cache

# Create your views here.

def signup(request):
	f = forms.SignUpForm()
	if request.method == "POST":
		f = forms.SignUpForm(request.POST)
		if f.is_valid():
			f.save(commit=False)	
			return  HttpResponseRedirect('/user/reg')
		else:
			print(f.errors)
	return render(request,'signup.html',{"form":f})

def log(request):
	f = forms.LoginForm()
	if request.method == "POST":
		f = forms.LoginForm(request.POST)
		if f.is_valid():
			cache.set('email',request.POST['email'],60)
			return HttpResponseRedirect('/profile/home')
		else:
			pass
	return render(request,'signin.html',{"form":f})

def registered(request):
	return render(request,'registered.html',{})
