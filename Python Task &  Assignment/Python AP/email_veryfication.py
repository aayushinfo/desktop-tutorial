#a@g.com min len <=6
#first letter only char
#only one @ 
#spical charcter not allow





email = input("Enter Your Email")

if len(email)>= 6:
    if email[0].isalpha():
        pass
    else:
        print("First letter always samll not big")

else:
    print("Min 6 Letter")