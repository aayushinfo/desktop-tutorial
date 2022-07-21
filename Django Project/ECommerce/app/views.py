import django
from django.shortcuts import render
from django.views import View
from .forms import CustomerRegistrationForm
from .models import *
from django.contrib import messages
# def home(request):
#  return render(request, 'app/home.html')
class ProductView(View):
    def get(self,request):
        topwear = Product.objects.filter(category="TW")
        jeans = Product.objects.filter(category="J")
        mobile = Product.objects.filter(category="M")
        return render(request,'app/home.html',{'topwear':topwear, 'jeans':jeans,'mobile':mobile})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == "realme" or data == 'vivo' or data == 'mi':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == "below":
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
    elif data == "above":
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
    return render(request, 'app/mobile.html',{'mobiles':mobiles})
    
def topwear(request,data=None):
    if data == None:
        topwears = Product.objects.filter(category='TW')
    elif data == "loki" or data == "random":
        topwears = Product.objects.filter(category="TW").filter(brand=data)
    elif data == "below":
        topwears = Product.objects.filter(category= "TW").filter(discounted_price__lt=500)
    elif data == "above":
        topwears = Product.objects.filter(category= "TW").filter(discounted_price__gt=500)
    return render(request ,"app/topwear.html",{'topwears':topwears})

def jeans(request, data=None):
    if data == None:
        jeans= Product.objects.filter(category="J")
    elif data == "sky" or data == "lee":
        jeans = Product.objects.filter(category="J").filter(brand = data)
    elif data == "below":
        jeans = Product.objects.filter(category= "J").filter(discounted_price__lt=500)
    elif data == "above":
        jeans = Product.objects.filter(category= "J").filter(discounted_price__gt=500)
    return render(request,'app/jeans.html',{'jeans':jeans})

def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#     return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form =CustomerRegistrationForm(request.POST)
        return render(request, 'app/customerregistration.html',{'form':form})
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Registered Suucessfully')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})


def checkout(request):
 return render(request, 'app/checkout.html')
