from django.db import models


# Create your models here.
class Users(models.Model):
    full_name = models.CharField(max_length=200),
    username = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField(null=True)
    password = models.CharField(max_length=100)
    year_of_birth = models.DateField(null=True)

    def __str__(self):  # return the value placed
        return self.username


class Products(models.Model):
    name = models.CharField(max_length=200)
    product_price = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    date = models.DateField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)