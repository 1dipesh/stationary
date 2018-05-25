from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib.auth import authenticate, login, get_user_model


def home_page(request):
	context = {
		"title" : "Hello world",
		"content":"Welcome to home page "


	}
	return render(request,"home_page.html",context)

def about_page(request):
	context = {
		"title" : "About Page",
		"content":"Welcome to about page "

	}
	return render(request,"home_page.html",context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)

	context = {
		"title" : "Contact",
		"content":"Welcome to contact page ",
		"form": contact_form


	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	return render(request,"contact/view.html",context)


