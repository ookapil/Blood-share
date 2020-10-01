from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db import models as gis_models


# Create your models here.
class blooddata(models.Model):
	name=models.CharField(max_length=100, default="kapil gyawali")
	age=models.IntegerField(default=5)
	bloodgroup=models.CharField(max_length=20)
	address=models.CharField(max_length=100)
	contact=models.CharField(max_length=50)

class position_donor(models.Model):
	position=gis_models.PointField()








