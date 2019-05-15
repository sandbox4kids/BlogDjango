from django.contrib import admin

# Register your models here.
from .models import Posts #Posts is the name of our model: see models.py

admin.site.register(Posts)