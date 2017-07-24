from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^signup/',views.signup,name='signup'),
	url(r'^login/',views.log,name='logcheck'),
	url(r'^reg/',views.registered,name='registered'),	
]