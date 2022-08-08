
from audioop import reverse
import re
from django.shortcuts import redirect, render
from .models import *
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    products = Products.objects.all()
    for i in products:
        i.market_price = i.product_price+300
    
    context = {
        "products" : products,
    }
    return render(request, "index.html", context=context)

    
   
def contact(request):
    if request.method == "POST":
        try:
            if request.POST["name"] == "" or request.POST["email"] == "" or request.POST["subject"] == "" or request.POST["message"] == "" or request.POST['category'] == "":
                context = {
                "msg_d" : "All fields are mandatory..."
            }
                return render(request, "contact.html", context=context)    
            else:
                contact = Contact.objects.create(
                    name = request.POST["name"],
                    email = request.POST["email"],
                    subject = request.POST["subject"],
                    message = request.POST["message"],
                    category = request.POST['category'],
                ) 
                contact.save()
              
                context = {
                    "msg_s" : "Contact request sent successfully..."
                }
                return render(request, "contact.html", context=context)
        except Exception as e:
            print(f"\n\n\n{e}\n\n\n")
            context = {
                "msg_d" : "Something went wrong..."
            }
            return render(request, "contact.html", context=context)
    else:
        return render(request, "contact.html")

def signup(request):
    if request.method == "POST":

        try:
            input_email = request.POST["email"]
            Buyer.objects.get(email = input_email)
            context = {
                "msg_d" : f"'{input_email}' is already registered with us...",
                "email" : input_email
            }
            return render(request, "signin.html", context=context)
        except:
            # try:
            if request.POST["fname"] == "" or request.POST["lname"] == "" or request.POST["email"] == "" or request.POST["phone"] == "" or request.POST["address"] == "" or request.POST["password"] == "" or request.POST["re_password"] == "": 
                context = {
                    "msg_d" : "*All fields are mandatory"
                }
                return render(request, "signup.html", context=context)    
            elif request.POST["password"] == request.POST["re_password"]:
                user = Buyer.objects.create(
                    fname = request.POST["fname"], 
                    lname = request.POST["lname"], 
                    email = request.POST["email"], 
                    phone = request.POST["phone"], 
                    address = request.POST["address"], 
                    password = request.POST["password"], 
                )
                user.save()
                
                context = {
                    "msg_s" : "Account created successfully",
                    "email" : user.email
                }
                return render(request, "signin.html", context=context)
            else:
                context = {
                    "msg_d" : "Password and Repeat Password does not match..."
                }
                return render(request, "signup.html", context=context)    
            # except Exception as e:
            #     print(f"\n\n\n{e}\n\n\n")
            #     context = {
            #         "msg_d" : "Something went wrong..."
            #     }
            #     return render(request, "signup.html", context=context)
    else:
        return render(request, "signup.html")

def signin(request):
    # if "email" in request.session:
    #     buyer = Buyer.objects.get(email =request.session['email'])
    #     context={
    #         'buyer':buyer
    #     }
    #     return render(request,"index.html",context=context)
    # else:
        if request.method == "POST":
            try:
                buyer = Buyer.objects.get(
                    email = request.POST["email"],
                )
                if buyer.email == request.POST["email"] and buyer.password == request.POST["password"]:
                    request.session["email"] = buyer.email
                    products = Products.objects.all()
                    context = {
                        "buyer" : buyer,
                        "products":products
                    }
                    return render(request, "index.html", context=context)
                else:
                    context = {
                        "msg_d" : "Id and password does not match..."
                    }
                    return render(request, "signin.html", context=context)
            except Exception as e:
                print(f"\n\n\n{e}\n\n\n")
                context = {
                    "msg_d" : "Email not registered..."            }
                return render(request, "signin.html", context=context)
        else:
            return render(request, "signin.html")


def signout(request):
    user_email = request.session["email"]
    del request.session["email"]
    context = {
        "msg_s" : "Logged out successfully...",
        "email" : user_email
    }
    return render(request, "signin.html", context=context)

def profile(request):
    user = Buyer.objects.get(email = request.session["email"])
    if request.method == "POST":
        user.fname = request.POST["fname"]
        user.lname = request.POST["lname"]
        user.phone = request.POST["phone"]
        user.address = request.POST["address"]
        user.save()
        return redirect("signout")
    else:
        context = {
            "user" : user
        }
        return render(request, "profile.html", context=context)

def change_password(request):
    user = Buyer.objects.get(email = request.session["email"])
    if request.method == "POST":
        try:
            if request.POST["old_password"] == "":
                context = {
                    "msg_d" : "Old password is necessary",
                    "user" : user
                }
                return render(request, "change_password.html", context=context)
            elif request.POST["new_password"] == request.POST["confirm_new_password"]:
                user.password = request.POST["new_password"]
                user.save()
                return redirect("signout")
            else:
                context = {
                    "msg_d" : "New password and confirm new password does not match...",
                    "user" : user
                }
                return render(request, "change_password.html", context=context)
        except Exception as e:
            print(f"\n\n\n{e}\n\n\n")
            context = {
                "msg_d" : "Something went wrong...",
                "user" : user
            }
            return render(request, "change_password.html", context=context)
    else:
        context = {
                "user" : user
            }
        return render(request, "change_password.html", context=context)


# def view_product(request, pk):
#     product = Products.objects.get(pk=pk)
#     buyer = Buyer.objects.get(buyer = buyer)
#     context = {
#         "product" : product,
#         "buyer" : buyer
#     }
#     return render(request, "view-product.html", context=context)













# seller section
def seller_index(request):
    try:
        seller = Seller.objects.get(email = request.session["email"])
        products = Products.objects.filter(seller = seller)
        context = {
            "products" : products,
        }
        return render(request, "seller_index.html", context=context)
    except Exception as e:
        print(f"\n\n\n\t\t{e}\n\n\n")
        context = {
            "msg_d" : "Login First",
        }
        return render(request, "seller_signin.html", context=context)

def seller_signin(request):
    if request.method == "POST":
        try:
            seller = Seller.objects.get(
                email = request.POST["email"],
            )
            if seller.email == request.POST["email"] and seller.password == request.POST["password"]:
                request.session["email"] = seller.email
                products=Products.objects.all()
                context = {
                    "seller" : seller,
                    "products":products
                }
                return render(request, "seller_index.html", context=context)
            else:
                context = {
                    "msg_d" : "Id and password does not match..."
                }
                return render(request, "seller_signin.html", context=context)
        except Exception as e:
            print(f"\n\n\n{e}\n\n\n")
            context = {
                "msg_d" : "Email not registered..."            }
            return render(request, "seller_signup.html", context=context)
    else:
        return render(request, "seller_signin.html")

def seller_signup(request):
    if request.method == "POST":
        try:
            input_email = request.POST["email"]
            Seller.objects.get(email = input_email)
            context = {
                "msg_d" : f"'{input_email}' is already registered with us...",
                "email" : input_email
            }
            return render(request, "seller_signin.html", context=context)
        except:
            # try:
            if request.POST["fname"] == "" or request.POST["company_name"] == "" or request.POST["email"] == "" or request.POST["phone"] == "" or request.POST["address"] == "" or request.POST["password"] == "" or request.POST["re_password"] == "": 
                context = {
                    "msg_d" : "*All fields are mandatory"
                }
                return render(request, "seller_signup.html", context=context)    
            elif request.POST["password"] == request.POST["re_password"]:
                user = Seller.objects.create(
                    fname = request.POST["fname"], 
                    company_name = request.POST["company_name"], 
                    email = request.POST["email"], 
                    phone = request.POST["phone"], 
                    address = request.POST["address"], 
                    password = request.POST["password"], 
                )
                user.save()
                subject = 'Account status : CREATED'
                message = f'Hi {user.fname}, Your account has been created successfully....'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )

                context = {
                    "msg_s" : "Account created successfully",
                    "email" : user.email
                }
                return render(request, "seller_signin.html", context=context)
            else:
                context = {
                    "msg_d" : "Password and Repeat Password does not match..."
                }
                return render(request, "seller_signup.html", context=context)    
            # except Exception as e:
            #     print(f"\n\n\n{e}\n\n\n")
            #     context = {
            #         "msg_d" : "Something went wrong..."
            #     }
            #     return render(request, "signup.html", context=context)
    else:
        return render(request, "seller_signup.html")

def seller_signout(request):
    user_email = request.session["email"]
    del request.session["email"]
    context = {
        "msg_s" : "Seller Logged out successfully...",
        "email" : user_email
    }
    return render(request, "seller_signin.html", context=context)

def add_product(request):
    try:
        seller = Seller.objects.get(email = request.session["email"]) 
        if request.method == "POST":
            if request.POST["product_name"] == "" or request.POST["product_price"] == "" or request.POST["stocks"] == "":
                context = {
                    "msg_d" : "All fields are mandatory but Description"
                }
                return render(request, 'seller_add_products.html', context=context)
            else:
                product = Products.objects.create(
                    seller = seller,
                    product_name = request.POST["product_name"],
                    product_price = request.POST["product_price"],
                    stocks = request.POST["stocks"],
                )

                if request.POST["desc"] == "":
                    product.desc = ""
                    product.save()
                else:
                    product.desc = request.POST["desc"]
                    product.save()
                    

                if "product_image" in request.FILES:
                    product.product_image = request.FILES["product_image"]
                    product.save()
                    context = {
                        "msg_s" : "Product uploaded successfully..."
                    }
                    
                    return render(request, 'seller_add_products.html', context=context)
                else:
                    context = {
                        "msg_w" : "Product uploaded with default image"
                    }
                    return render(request, 'seller_add_products.html', context=context)
        else:
            return render(request, 'seller_add_products.html')
    except Exception as e:
        print(f"\n\n\n{e}\n\n\n")
        context = {
            "msg_d" : "Something went wrong..."
        }
        return render(request, 'seller_add_products.html', context=context)

def view_product_seller(request, pk):
    seller = Seller.objects.get(email = request.session["email"])
    product = Products.objects.get(pk=pk)
    context = {
        "product" : product,
        "seller" : seller,
    }
    return render(request, "view-product-seller.html", context=context)

def edit_product_seller(request, pk):
    seller = Seller.objects.get(email = request.session["email"])
    product = Products.objects.get(seller=seller, pk=pk)

    context = {
        "product" : product,
        "seller" : seller, 
    }

    if request.method == "POST":
            if request.POST["product_name"] == "" or request.POST["product_price"] == "" or request.POST["stock"] == "":
                context.update({
                    "msg_d" : "All fields are mandatory but Description",
                })
                return render(request, 'edit-product-seller.html', context=context)
            else:
                product.product_name = request.POST["product_name"] 
                product.product_price = request.POST["product_price"] 
                product.stock = request.POST["stock"] 
                product.save()

                if request.POST["desc"] == "":
                    product.desc = ""
                    product.save()
                else:
                    product.desc = request.POST["desc"]
                    product.save()
                    

                if "product_image" in request.FILES:
                    product.product_image = request.FILES["product_image"]
                    product.save()
                    context.update({
                        "msg_s" : "Product updated successfully..."
                    })
                    return render(request, 'edit-product-seller.html', context=context)
                else:
                    context.update({
                        "msg_s" : "Product updated successfully..."
                    })
                    return render(request, 'edit-product-seller.html', context=context)
    else:
        context = {
            "product" : product,
            "seller" : seller, 
        }
        return render(request, "edit-product-seller.html", context=context)

def delete_product_seller(request, pk):
    seller = Seller.objects.get(email = request.session["email"])
    product = Products.objects.get(seller=seller, pk=pk)
    
    product.delete()

    return redirect("seller_home")
def view_product(request,pk):
    seller = Seller.objects.get(email = request.session["email"])
    product = Products.objects.get(pk=pk)
    context = {
        "product" : product,
        "seller" : seller,
    }
    return render(request, "view_product.html", context=context)
