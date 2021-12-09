from django.contrib import admin

# Register your models here.
from .models import Customer, Phone, Email

# admin.site.register(Customer)
admin.site.register(Phone)
admin.site.register(Email)


class PhoneInline(admin.StackedInline):
    model = Phone
    extra = 0


class EmailInline(admin.StackedInline):
    model = Email
    extra = 0


class CustomerAdmin(admin.ModelAdmin):
    """
    Define the admin class
    """
    inlines = [PhoneInline, EmailInline]


admin.site.register(Customer, CustomerAdmin)
"""
 Register the admin class with the associated model
"""