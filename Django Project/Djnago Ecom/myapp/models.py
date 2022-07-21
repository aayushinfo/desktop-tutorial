from distutils.command.upload import upload
import email
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    remarks = models.TextField()

    def __str__(self):
        return self.email


class User(models.Model):
    fname = models.TextField(max_length=100)
    lname = models.TextField(max_length=100)
    email = models.EmailField()
    mobile = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    profile_pic = models.ImageField(upload_to = "profile_pic/")

    def __str__(self):
        return self.fname + " " + self.lname