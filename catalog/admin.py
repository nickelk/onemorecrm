from django.contrib import admin

# Register your models here.
from .models import Customer, Phone, Email

admin.site.register(Customer)
admin.site.register(Phone)
admin.site.register(Email)
