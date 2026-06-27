from django.contrib import admin
from .models import Products
from .models import Car
from .models import Student
# Register your models here.
admin.site.register(Products)
admin.site.register(Car)
admin.site.register(Student)