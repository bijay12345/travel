from django.contrib import admin
from .models import TravelDestination,DestinationImages


@admin.register(TravelDestination)
class TravelDestinationAdmin(admin.ModelAdmin):
	list_display=['id','name','location','price_package']


admin.site.register(DestinationImages)