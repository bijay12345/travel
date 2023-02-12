from django.db import models
from django.contrib.auth.models import User


class TravelDestination(models.Model):
	name=models.CharField(max_length=200)
	description = models.TextField()	
	images=models.ForeignKey("DestinationImages",on_delete=models.SET_NULL,null=True,blank=True)
	price_package=models.DecimalField(max_digits=8, decimal_places=2)
	price_discount=models.DecimalField(max_digits=8, decimal_places=2)
	location=models.CharField(max_length=100)
	likers=models.ManyToManyField(User,related_name="likers",null=True,blank=True)
	distance=models.IntegerField()


	def __str__(self):
		return self.name

class DestinationImages(models.Model):
	destination=models.ForeignKey(TravelDestination,on_delete=models.CASCADE)
	image=models.ImageField(upload_to="destination",default="default.jpg")
