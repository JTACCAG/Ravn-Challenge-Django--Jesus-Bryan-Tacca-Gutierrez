from django.contrib import admin
from .models import Person, People, Vehicles
# Register your models here.


admin.site.register(People)
admin.site.register(Person)
admin.site.register(Vehicles)