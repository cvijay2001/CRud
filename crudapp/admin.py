from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Employee)
class Emp(admin.ModelAdmin):
    list_display=['eid','ename','eemail','econtact','eprofilephoto']
