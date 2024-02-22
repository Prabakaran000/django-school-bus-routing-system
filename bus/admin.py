from django.contrib import admin
from .models import SchoolBus, Routes, Students

admin.site.register(SchoolBus)
admin.site.register(Routes)
admin.site.register(Students)