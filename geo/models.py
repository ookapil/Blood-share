from django.db import models
from django.contrib.gis.db import models as gis_models
# Create your models here.
#getting models form gismodel.py
class District(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    dcode = models.IntegerField(blank=True, null=True)
    dist_name = models.CharField(max_length=18, blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=6, decimal_places=6, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=6, decimal_places=6, blank=True, null=True)
    code1 = models.SmallIntegerField(blank=True, null=True)
    geom = gis_models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'District'
