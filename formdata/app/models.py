from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Form(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.TextField()
    whatsapp = models.CharField(max_length=256)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()
    cnic = models.CharField(max_length=20)
    profession = models.CharField(max_length=256, default='')
    organization = models.CharField(max_length=256, default='')
    designation = models.CharField(max_length=256, default='')
    monthly_income = models.CharField(max_length=10)
    working_since = models.DateField(default='')
    qualification = models.CharField(max_length=256, default='')