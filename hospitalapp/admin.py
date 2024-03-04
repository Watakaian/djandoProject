from django.contrib import admin
from hospitalapp import models
#from hospitalapp.models import Users,Products,Member,Appointment,Contact,
# Register your models here.
admin.site.register(models.Users)
admin.site.register(models.Products)
admin.site.register(models.Member)
admin.site.register(models.Appointment)
admin.site.register(models.Contact)
admin.site.register(models.ImageModel)
