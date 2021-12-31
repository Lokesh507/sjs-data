from django.db import models
from datetime import date
# Create your models here.


class Vehicle_Data(models.Model):
    vehicle_no = models.CharField(max_length=100)
    vehicle_arrived_date = models.DateField()
    vehicle_wash = models.CharField(max_length=50)
    vehicle_amount = models.IntegerField(default=0)
    payment_type = models.CharField(max_length=50)


class sjs_dailyprofit(models.Model):
    dialy_date = models.DateField(default=date.today())
    dialy_profit = models.IntegerField(default=0)
