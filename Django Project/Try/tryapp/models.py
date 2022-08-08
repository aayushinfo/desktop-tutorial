from distutils.command.upload import upload
import email
from email.policy import default
from itertools import product
from pyexpat import model
from unicodedata import category
from warnings import catch_warnings
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=210)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name

class Buyer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self) -> str:
        return self.fname 

class Seller(models.Model):
    fname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(unique=True)
    address = models.TextField()
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.fname + " | " + self.company_name


CHOOSE_CATEGORY = (
    ("J",'Jeans'),
    ("TW",'Top Wear'),
    ("M","Mobile"),
)


class Products(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,blank=True,null=True)
    product_name = models.CharField(max_length=100,default="")
    product_price = models.PositiveIntegerField()
    product_image = models.ImageField(upload_to = "images/products/",default="")
    desc = models.TextField()
    stocks = models.PositiveIntegerField(default=1)
    category = models.CharField(choices=CHOOSE_CATEGORY,max_length=4,default="")
    def __str__(self) -> str:
        return self.product_name