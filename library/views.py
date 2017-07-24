from django.shortcuts import render

def home(request):
	# print(dir(request.session))
	return render(request,'index.html',{})