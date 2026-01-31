# Ex01 Django ORM Web Application
## Date: 31.01.2026

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
~~~
model.py
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

admin.py
from django.contrib import admin
from .models import FoodDB,FoodDBAdmin 
admin.site.register(FoodDB,FoodDBAdmin)
~~~


## OUTPUT
![alt text](<Screenshot (18).png>)


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
