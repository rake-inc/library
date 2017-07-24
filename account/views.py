from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from signin.models import SignUp , Book 

# Create your views here.
data_key = {}

for i in SignUp.objects.all():
	data_key[i.email] = i.name


def testing(request):
	cached_data = cache.get('email')
	return HttpResponse("<h3>Hi "+ str(data_key[cached_data]) +"</h3>")