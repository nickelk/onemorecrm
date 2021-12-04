from django.contrib import admin

# Register your models here.
from .models import Customer, Phone, Email, Project, Interaction

admin.site.register(Customer)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Project)
admin.site.register(Interaction)
