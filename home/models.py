from django.db import models

# Create your models here.
class PJ(models.Model):
    ten_pj = models.CharField(max_length=30)
    duong_dan = models.CharField(max_length=100)