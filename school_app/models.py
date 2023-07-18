from django.db import models

# Create your models here.


class Student(models.Model):
	name = models.CharField(max_length=60)
	updated = models.DateTimeField(auto_now = True)
	joined = models.DateTimeField(auto_now_add=True, null=True)
	Class = models.IntegerField()
	parent_name = models.CharField(max_length=60, null=True)
	parent_email = models.EmailField()
	bus_number = models.CharField(max_length=10)
	password = models.CharField(max_length=25,default='')

	def __str__(self):
		return self.name


class Bus(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Driver(models.Model):
    bus_number = models.CharField(max_length=10)
    driver_name = models.CharField(max_length=60)
    phone_number = models.IntegerField()
    updated = models.DateTimeField(auto_now = True)
    joined = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.driver_name

class FeedBacks(models.Model):
	name = models.CharField(max_length=60)
	joined = models.DateTimeField(auto_now_add=True, null=True)
	email = models.EmailField()
	message = models.TextField(max_length=500)

	def __str__(self):
		return self.name