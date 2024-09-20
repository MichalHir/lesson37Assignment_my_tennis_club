from django.contrib import admin
from .models import Court

# Register your models here.

class CourtAdmin(admin.ModelAdmin):
  list_display = ("number", "is_occupied")
  
admin.site.register(Court, CourtAdmin)
