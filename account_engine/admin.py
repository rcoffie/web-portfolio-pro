from django.contrib import admin
from account_engine.models import Profile
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class ProfileAdmin(LeafletGeoAdmin):
    pass
    
admin.site.register(Profile, ProfileAdmin)
