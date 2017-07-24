from django.db import models

# Create your models here.

class SignUp(models.Model):
	name = models.CharField(max_length=32,blank=True,null=False)
	email = models.EmailField(null=False,unique=True,blank=True)
	password = models.CharField(max_length=128,blank=True,null=False)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	# img = models.FileField(null=False,blank=True)

	def __str__(self):
		return self.email

class Book(models.Model):
	bookName = models.CharField(max_length=32,unique=True)
	authorName = models.CharField(max_length=32)
	numberOfBooks = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.bookName