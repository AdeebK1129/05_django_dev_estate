from django.contrib import admin
from listings.models import Property, PropertyFeatures, Agent, PropertyAgent, School, PropertySchool, PriceHistory, NearbyHomes

# Register your models here.
admin.site.register(Property)
admin.site.register(Agent)
