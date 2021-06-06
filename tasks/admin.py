from django.contrib import admin

# Register your models here.
from .models import *
# Register the class name from models.py inside admin.site.register()
admin.site.register(Task)