from django.contrib import admin

from .models import PersonDetail

# Register your models here.

class PersonDetailAdmin(admin.ModelAdmin):
    list_display = ("__str__", "matriz")

    
admin.site.register(PersonDetail, PersonDetailAdmin)
