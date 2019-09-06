from django.contrib import admin
from . models import Listing, Coverage
# Register your models here.

# admin.site.register(Listing)
# admin.site.register(Coverage)
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['name', 'rate_of_interest', 'created_on']
    list_filter = ['name']

@admin.register(Coverage)
class CoverageAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'created_on']
    list_filter = ['name']

