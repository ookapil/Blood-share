from django.shortcuts import render
from django.http import HttpResponse
from django.http import *
from . models import blooddata
from django.db.models import Q
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return render(request,'index.html')

def donate(request):
	return render(request,'donate.html')

def register_doner(request):
	if request.method=="POST":
		first_name= request.POST['first_name']
		last_name= request.POST['last_name']
		name= first_name + last_name
		age= request.POST['age']
		blood_group= request.POST['blood_group']
		contact= request.POST['contact']
		address= request.POST['address']
		blooddata.objects.create(name=name, age=age, bloodgroup=blood_group, address=address, contact=contact)
	return HttpResponseRedirect("/")

def search(request):
	return render(request, 'search.html')

def result(request):
	if (request.method=="POST"):
		group=request.POST['bloodgroup']
		city=request.POST['city']

		if (group,city):
			match= blooddata.objects.filter(Q(bloodgroup__icontains=group), Q(address__icontains=city))

			if match:
				return render(request, 'result.html', {'match':match})
			else:
				messages.error(request,"No result found")
		else:
			return HttpResponseRedirect('/receive/')
			
		if group:
			match= blooddata.objects.filter(Q(bloodgroup=group))

			if match:
				return render(request, 'result.html', {'match':match})
			else:
				messages.error(request,"No result found")
		else:
			return HttpResponseRedirect('/receive/')


