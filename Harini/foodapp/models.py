from django.db import models
from django.contrib import admin
class FoodDB(models.Model):
	Date=models.DateField();
	OrderNo=models.IntegerField(primary_key=True);
	CustomerName=models.CharField(max_length=10);
	MobileNo=models.IntegerField();
	FoodName=models.CharField(max_length=12);
	Amount=models.FloatField();
	Address=models.CharField(max_length=20);
class FoodDBAdmin(admin.ModelAdmin):
	list_display=['Date','OrderNo','CustomerName','MobileNo','FoodName','Amount','Address']
    

