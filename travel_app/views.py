from django.shortcuts import render
from .serializers import TravelDestinationSerializer,DestinationImagesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TravelDestination,DestinationImages


class TravelApi(APIView):
	def get(self,request,format=None):
		destinations=TravelDestination.objects.all()
		serializer=TravelDestinationSerializer(destinations,many=True)
		return Response({"destinations":serializer.data})

