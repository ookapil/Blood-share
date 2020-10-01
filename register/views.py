from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate


# Create your views here.
def Register(request):
	return render(request, "register.html")

def success(request):
	if request.method=='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		email=request.POST['email']
		username=request.POST['username']
		password_1=request.POST['password_1']
		password_2=request.POST['password_2']
		if password_1==password_2:
			if User.objects.filter(username=username).exists():
				messages.info(request,"Username taken")
				return redirect('register')

			elif User.objects.filter(email=email).exists():
				messages.info(request, "email already in use")
				return redirect('register_app:register')
			
			else:
				user=User.objects.create(first_name=first_name, last_name=last_name, username=username,
					email=email, password=password_1)
				user.save()
				return redirect('register_app:login')
				print(email)
		
		else:
			messages.info(request, 'password not matching')
			return redirect('register_app:register')



def login(request):
	return render(request, 'login.html')



def login_success(request):
	if request.method=='POST':
		username=request.POST['user']
		password=request.POST['pass']
		print(username)
		print(password)
		user= auth.authenticate(request, username=username, password=password)
		print(user)

		if user is not None:
			auth.login(request, user)
			return redirect('/')

		else:
			messages.info(request, "Username or password is not matching" )
			return redirect('register_app:login')


			

