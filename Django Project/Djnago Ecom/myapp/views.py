
import email
from errno import ESTALE
from re import U
import re
from tkinter.messagebox import RETRY
from django.db import reset_queries
from django.shortcuts import redirect, render
from .models import Contact, User
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            mobile = request.POST['mobile'],
            remarks = request.POST['remarks']
        )
        contacts = Contact.objects.all().order_by('-id')[:5]
        msg = "Contact Save Succesfully"
        return render(request,"contact.html",{'contacts' : contacts, 'msg' : msg})
    else:    
        contacts = Contact.objects.all().order_by('-id')[:5]
        return render(request,"contact.html",{'contacts' : contacts})

def signup(request):
    if request.method == "POST":
      
        try:
            User.objects.get(email = request.POST['email'])
            msg = "Email Allready registerd "
            return render(request,"signup.html",{'msg':msg})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                    fname = request.POST['fname'],
                    lname = request.POST['lname'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    password = request.POST['password'],
                    address = request.POST['address'],
                    profile_pic = request.FILES['profile_pic']
                )
                msg = "Signup Succesfully"
                return render(request,'signin.html',{'msg':msg})
            else:
                msg = "Password and Confirm Password Does not match"
                return render(request, "signup.html",{'msg':msg})
    else:
        return render(request,"signup.html")

def signin(request):
    if request.method == "POST":
        try:
            user=User.objects.get(email=request.POST['email'],password=request.POST['password'])
            request.session['email']=user.email
            request.session['fname']=user.fname
            request.session['profile_pic'] = user.profile_pic.url
            return render(request,"index.html")
        except:
            msg = "Email or Password is Wrong"
            return render(request,"signin.html",{'msg':msg})
    else:
        return render(request,"signin.html")

def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        return render(request ,'signin.html')
    except:
        return render(request, 'index.html')

def change_password(request):
    if request.method == "POST":
        user = User.objects.get(email = request.session['email'])
        if user.password == request.POST['old_password']:
            if request.POST['new_password'] == request.POST['cnew_password']:
                user.password=request.POST['new_password']
                user.save()
                return redirect('logout')
            else:
                msg="New password and confirm new password does not match"
                return render(request,"change_password.html",{'msg':msg})
        else:
            msg = "Old password does not match"
            return render(request,"change_password.html",{'msg':msg})
    else:
        return render(request,'change_password.html')

def forgot_password(request):
    if request.method == "POST":
        try:
            otp = random.randint(1000,9999)
            user = User.objects.get(email = request.POST['email'])    
            subject = 'Forgot Password'
            message = 'Your otp is'+str(otp)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,"otp.html",{'otp':otp,'email':user.email})
        except:
            msg = "Email does not exit"
            return render(request,"forgot_password.html",{'msg':msg})
    else:
            return render(request,"forgot_password.html")

def verify_otp(request):
    otp1 = request.POST['otp1']
    otp2 = request.POST['otp2']
    email = request.POST['email']

    if otp1 == otp2:
        return render(request,'new_password.html',{'email':email})
    else:
        msg = "Invalid OTP"
        return render(request,'otp.html',{'msg':msg,'otp1':otp1,'email':email})


def new_password(request):
    email = request.POST['email']
    np = request.POST['new_password']
    cnp = request.POST['cnew_password']

    if np == cnp:
        user = User.objects.get(email=email)
        user.password = np
        user.save()
        return render(request,'signin.html')
    
    else:
        msg = "New Password And Confirm New Password Does Not Match"
        return render(request,"new_password.html",{'msg':msg,'email':email})