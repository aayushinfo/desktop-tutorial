
from distutils.command.upload import upload
import email
from pyexpat import model
from tkinter import CASCADE
from unicodedata import name
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    title = models.CharField(max_length=200 , null=True , blank=True)
    comments = models.TextField()

    def __str__(self) -> str:
        return self.name + " " +self.email

class Signup(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=300)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name + " " +self.email

class Seller(models.Model):
    name = models.CharField(max_length=300)
    c_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.c_name + " \ " + self.email


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True, null=True)
    product_name = models.CharField(max_length=100)
    product_price = models.PositiveBigIntegerField()
    product_image = models.ImageField(upload_to = "images/products/")
    desc = models.TextField(blank=True , null=True)
    stock = models.PositiveBigIntegerField(default=1)