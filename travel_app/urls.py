from .views import TravelApi
from django.urls import path  


urlpatterns = [
	path("",TravelApi.as_view(),name="travel"),
]