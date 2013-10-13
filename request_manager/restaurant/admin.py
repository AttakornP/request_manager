from django.contrib import admin
from models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
