from operator import index
from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='home'),
    path("contact/", contact, name='contact'),
    path("signup/",signup,name="signup"),
    path("signin/", signin,name="signin"),
    path("signout/",signout,name="signout"),
    path("myaccount/",myaccount,name="myaccount"),
    path("change_password/",change_password,name="change_password"),


    path("seller_home/",seller_home,name="seller_home"),
    path("seller_signin/",seller_signin,name="seller_signin"),
    path("seller_signup/",seller_signup,name="seller_signup"),
    path("seller_signout/",seller_signout,name="seller_signout"),
    path("seller_add_products",seller_add_products,name="seller_add_products"),

    
]
