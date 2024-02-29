from django.contrib import admin
from hospitalapp.models import Users,Products,Member,Appointment,Contact
# Register your models here.
admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Member)
admin.site.register(Appointment)
admin.site.register(Contact)