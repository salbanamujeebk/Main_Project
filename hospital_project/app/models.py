from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, is_password_usable
# Create your models here.



class CustomUser(AbstractUser):
    Phonenumber=models.IntegerField(null=True,blank=True,unique=True)
    Age=models.IntegerField(null=True,blank=True)
    Address=models.CharField(null=True,blank=True,max_length=100)
    DOB=models.DateField(null=True,blank=True)
    usertype=models.CharField(max_length=200)



class Departments(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()

    def __str__(self):
            return self.dep_name


class Doctors(models.Model):
    doc = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    speciality=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    # department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    image=models.FileField()

    def __str__(self):
         return self.name





class Booking(models.Model):
    p_name=models.CharField(max_length=200)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    name=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)


class Emergency(models.Model):
     p_heading=models.CharField(max_length=200)
     p_description=models.TextField()


class Orpahan_care(models.Model):
     heading=models.CharField(max_length=200)
     description=models.TextField()
     


class PatientConsultation(models.Model):
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    state = models.CharField(max_length=100)
    condition = models.TextField()
    medicine = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
