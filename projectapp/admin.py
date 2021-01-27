from django.contrib import admin
from projectapp.models import *
class AdminData(admin.ModelAdmin):
    list_display = ['Title','Content','Image']

admin.site.register(WriterData,AdminData)
