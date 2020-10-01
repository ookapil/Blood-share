# Generated by Django 3.0.8 on 2020-08-26 10:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodshare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('objectid', models.IntegerField(blank=True, null=True)),
                ('dcode', models.IntegerField(blank=True, null=True)),
                ('dist_name', models.CharField(blank=True, max_length=18, null=True)),
                ('shape_leng', models.DecimalField(blank=True, decimal_places=6, max_digits=6, null=True)),
                ('shape_area', models.DecimalField(blank=True, decimal_places=6, max_digits=6, null=True)),
                ('code1', models.SmallIntegerField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=0)),
            ],
            options={
                'db_table': 'districts',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Districts',
        ),
    ]
