from django.shortcuts import render
from django.http import HttpResponse
from . models import District
from django.core.serializers import serialize


# Create your views here.
def index(request):
	return render(request, 'geo_home.html')

# def  get_district(request):
# 	district=serialize("geojson",District.objects.all())
# 	return HttpResponse("json",district)
		

