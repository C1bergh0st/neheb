from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Organization)
admin.site.register(models.Attendee)
admin.site.register(models.Tag)
admin.site.register(models.ItemType)
admin.site.register(models.Ribbon)
admin.site.register(models.Item)
admin.site.register(models.Transaction)