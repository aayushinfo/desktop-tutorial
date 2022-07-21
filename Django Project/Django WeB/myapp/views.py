from django.shortcuts import redirect, render
from .models import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, 'home.html') 

def contact(request):
    if request.method == "POST":
        try:
            if request.POST["name"] == "" or request.POST["email"] == "" or request.POST["title"] == "" or request.POST["comments"] == "":
                context = {
                    "msg_d" : "All fields are mandatory..."
                }
                return render(request,"contact.html",context=context)
            else:
                contact = Contact.objects.create(
                    name = request.POST["name"],
                    email = request.POST["email"],
                    title = request.POST["title"],
                    comments = request.POST["comments"],
                )
                contact.save()
                subject = 'Message sent status : SUCCESSFUL'
                message = f'Hi {contact.name}, thank you for contatcting us.\n\n Our team will get back to you soon. \n\n Best Regards...'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [contact.email, ]
                send_mail( subject, message, email_from, recipient_list )

                subject = f'Contact request sent by {contact.name}'
                message = f'SUBJECT{contact.title} \n\n COMMENTS{contact.comments}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [settings.EMAIL_HOST_USER]
                send_mail( subject, message, email_from, recipient_list )


                context =  {
                    "msg_s" : "Contact request sent successfully..."
                }
                return render(request,"contact.html",context=context)
        except Exception as e:
            print(f"\n\n{e}\n\n")
            context =  {
                "msg_d" : "Something went wrong..."
            }
            return render(request,"contact.html",context=context)
    else:
        return render(request,"contact.html")    



def signup(request):
    if request.method == "POST":

        try:
            input_email = request.POST["email"]
            Signup.objects.get(email = input_email)
            context = {
                "msg_d" : f"'{input_email}' is already registered with us...",
                "email" : input_email
            }
            return render(request, "sign-in.html", context=context)
        except:
            try:
                if request.POST["email"] == "" or request.POST["name"] == "" or request.POST["phone"] == "" or request.POST["password"] == "" or request.POST["c_password"] == "": 
                    context = {
                        "msg_d" : "*All fields are mandatory"
                    }
                    return render(request, "signup.html", context=context)    
                elif request.POST["password"] == request.POST["c_password"]:
                    user = Signup.objects.create(
                        email = request.POST["email"], 
                        name = request.POST["name"],
                        phone = request.POST["phone"], 
                        password = request.POST["password"], 
                    )
                    user.save()
                    subject = 'Account status : CREATED'
                    message = f'Hi {user.name}, Your account has been created successfully....'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [user.email, ]
                    send_mail( subject, message, email_from, recipient_list )

                    context = {
                        "msg_s" : "Account created successfully",
                        "email" : user.email
                    }
                    return render(request, "sign-in.html", context=context)
                else:
                    context = {
                        "msg_d" : "Password and Repeat Password does not match..."
                    }
                    return render(request, "sign-up.html", context=context)    
            except Exception as e:
                print(f"\n\n\n{e}\n\n\n")
                context = {
                    "msg_d" : "Something went wrong..."
                }
                return render(request, "sign-up.html", context=context)
    else:
        return render(request, "sign-up.html")



def signin(request):
    if request.method == "POST":
        try:
            buyer = Signup.objects.get(
                email = request.POST["email"],
            )
            if buyer.email == request.POST["email"] and buyer.password == request.POST["password"]:
                request.session["email"] = buyer.email
                context = {
                    "buyer" : buyer,
                }
                return render(request, "home.html", context=context)
            else:
                context = {
                    "msg_d" : "Id and password does not match..."
                }
                return render(request, "sign-in.html", context=context)
        except Exception as e:
            print(f"\n\n\n{e}\n\n\n")
            context = {
                "msg_d" : "Email not registered..."
            }
            return render(request, "sign-in.html", context=context)
    else:
        return render(request, "sign-in.html")


def signout(request):
    
    del request.session["email"]
    context = {
        "msg_s" : "Logged out successfully..."
    }
    return render(request, "sign-in.html", context=context)


def myaccount(request):
    user = Signup.objects.get(email = request.session["email"])
    if request.method == "POST":
        user.email = request.POST["email"]
        user.name = request.POST["name"]
        user.phone = request.POST["phone"]
        user.save()
        return redirect("signout")
    else:
        context = {
            "user" : user
        }
        return render(request, "myaccount.html", context=context)



def change_password(request):
    user = Signup.objects.get(email = request.session["email"])
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





#seller

def seller_home(request):
    try:
        seller = Seller.objects.get(email = request.session["email"])
        products = Product.objects.filter(seller = seller)
        context = {
            "products" : products,
        }
        return render(request, "seller_home.html", context=context)
    except Exception as e:
        print(f"\n\n\n\t\t{e}\n\n\n")
        context = {
            "msg_d" : "Something went wrong...",
        }
        return render(request, "seller_signin.html", context=context)



def seller_signin(request):
    if request.method == "POST":
        try:
            seller = Seller.objects.get(
                email = request.POST["email"],
            )

            print("\n\n\nSeller found\n\n\n")

            if seller.email == request.POST["email"] and seller.password == request.POST["password"]:
                request.session["email"] = seller.email
                context = {
                    "seller" : seller
                }
                print("\n\n\nSeller logged in\n\n\n")

                return render(request,"seller_home.html",context=context)
            else:
                context = {
                    "msg_d" : "ID and password does not match..."
                }
                print("\n\n\nSeller logged in\n\n\n")
                return render(request,"seller_signin.html", context=context)
        except Exception as e:
            print(f"/n/n/n{e}/n/n/n")
            context = {
                "msg_d" : "Email not registered..."
            }
            print("\n\n\Exception raised\n\n\n")
            return render(request,"seller_signup.html",context=context)
    else:
        print("\n\n\nI am in else block\n\n\n")
        return render(request,"seller_signin.html")



                    
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
            if request.POST["name"] == "" or request.POST["c_name"] == "" or request.POST["email"] == "" or request.POST["phone"] == "" or request.POST["password"] == "" or request.POST["c_password"] == "": 
                context = {
                    "msg_d" : "*All fields are mandatory"
                }
                return render(request, "seller_signup.html", context=context)    
            elif request.POST["password"] == request.POST["c_password"]:
                user = Seller.objects.create(
                    name = request.POST["name"], 
                    c_name = request.POST["c_name"], 
                    email = request.POST["email"], 
                    phone = request.POST["phone"], 
                    password = request.POST["password"], 
                )
                user.save()
                subject = 'Account status : CREATED'
                message = f'Hi {user.name}, Your account has been created successfully....'
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
    
    del request.session["email"]
    context = {
        "msg_s" : "Logged out successfully..."
    }
    return render(request, "seller_signin.html", context=context)



def seller_add_products(request):
    try:
        seller = Seller.objects.get(email = request.session["email"]) 
        if request.method == "POST":
            if request.POST["product_name"] == "" or request.POST["product_price"] == "" or request.POST["stock"] == "":
                context = {
                    "msg_d" : "All fields are mandatory but Description"
                }
                print("All fields are mandatory but Description")
                return render(request, 'seller_add_products.html', context=context)
            else:
                product = Product.objects.create(
                    seller = seller,
                    product_name = request.POST["product_name"],
                    product_price = request.POST["product_price"],
                    stock = request.POST["stock"],
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
                    print("Product uploaded successfully")
                    return render(request, 'seller_add_products.html', context=context)
                else:
                    context = {
                        "msg_w" : "Product uploaded with default image"
                    }
                    print("Product uploaded with default image")
                    return render(request, 'seller_add_products.html', context=context)
        else:
            print("nooooooooo")
            return render(request, 'seller_add_products.html')
    except Exception as e:
        print(f"\n\n\n{e}\n\n\n")
        context = {
            "msg_d" : "Something went wrong..."
        }
        print("Something went wrong...")
        return render(request, 'seller_add_products.html', context=context)

