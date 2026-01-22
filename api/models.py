
# Create your models here.
from django.db import models

class Voter(models.Model):
    ward_no = models.IntegerField()
    ac_no = models.IntegerField()
    ps_no = models.IntegerField()
    sl_no = models.IntegerField()
    name = models.CharField(max_length=100)
    relation_name = models.CharField(max_length=100)
    relation = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    door_no = models.CharField(max_length=50)
    epic_no = models.CharField(max_length=20)
