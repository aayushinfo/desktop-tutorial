from django.shortcuts import render
from django.http import HttpResponse
from store.models.category import Category
from .models.product import Product
from .models.customer import Customer
from store.models import customer


# Create your views here.

def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')

    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();


    data = {}
    data["products"] = products
    data["categories"] = categories
    return render(request, 'index.html', data )


def signup(request):
    if request.method == "GET":
        return render(request ,"signup.html")
    else:
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        print(first_name, last_name , email)
        customer = Customer(
        first_name=first_name,
        last_name = last_name, 
        phone = phone, 
        email = email, 
        password = password)
        customer.register() 
        #aa rigister aapre j cistomer.py ma banavyu che a che aa customer ne save j karshe ane em na karvu hoy to aapre dirct customer.save() pan kari shake che.
        return HttpResponse("signup success")