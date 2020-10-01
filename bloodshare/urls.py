from django.urls import path
from . import views

app_name='bloodshare_app'

urlpatterns=[
	path('',views.index, name='index'),
	path('donate',views.donate, name="donate"),
	path('register_doner',views.register_doner, name="register"),
	path('receive',views.search, name="search"),
	path('result',views.result, name="result"),
	
	]