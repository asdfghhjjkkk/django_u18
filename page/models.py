from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    engine_type = models.CharField(max_length=50)
    horsepower = models.IntegerField()
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=30)
    transmission = models.CharField(max_length=30)
    is_available = models.BooleanField(default=True)
    vin_number = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()
    grade = models.CharField(max_length=10)
    gpa = models.FloatField()
    attendance_percentage = models.FloatField()
    is_active = models.BooleanField(default=True)
    emergency_contact = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
