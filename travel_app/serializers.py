from rest_framework import serializers
from .models import TravelDestination,DestinationImages
from django.core.exceptions import ObjectDoesNotExist

class TravelDestinationSerializer(serializers.ModelSerializer):
	front_image=serializers.SerializerMethodField()

	def get_front_image(self,obj):
		url=""
		try:
			image=DestinationImages.objects.filter(destination=obj)
			if len(image) > 0:	
				url=image[0].image.url
			else:
				url="None"
		except ObjectDoesNotExist:
			url="None"
		return url


	class Meta:
		model=TravelDestination
		fields="__all__"

class DestinationImagesSerializer(serializers.ModelSerializer):
	class Meta:
		model=DestinationImages
		fields="__all__"