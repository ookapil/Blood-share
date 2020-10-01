from django.urls import path
from . import views

urlpatterns=[
	path('',views.index, name='index'),
	# path('get_district',views.get_district, name="get_district"),
	
]