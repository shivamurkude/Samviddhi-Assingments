from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.

class TAAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TA._meta.fields]


admin.site.register(TA,TAAdmin)