# age = int(input("enter your age:-"))
# if age >= 18:
#     print("yes")
# else:
#     print("noo")

# a = int(input("Enter number:- "))
# b = int(input("Enter number:- "))
# c = int(input("Enter number:- "))
# d = int(input("Enter number:- "))

# if a > d:
#     f1 = a
# else:
#     f1 = d

# if b > c:
#     f2 = b
# else:
#     f2 = c

# if f1 > f2:
#     print(str(f1) + " is big")
# else:
#     print(str(f2) + "is big")

# if a > d:
#     if a > c:
#         if a > d:
#             print("a is big")
#         else:
#             print("d is big")
#     if c > d:
#         print("c is big")
#     else:
#         print("d is big")
# else:
#     if b > c:
#         if b > d:
#             print("b is big")
#         else:
#             print("d is big")
#     else:
#         if c > d:
#             print("c is big")
#         else:
#             print("d is big")

# sub1 = int(input("enter sub1 marks:- "))
# sub2 = int(input("enter sub2 marks:- "))
# sub3 = int(input("enter sub3 marks:- "))

# if sub1 < 33 or sub2 < 33 or sub3 < 33:
#     print("you are fali becuse you have less than 33% in one subject")
# elif (sub1 + sub2 + sub3) / 3 < 40:
#     print("you are fail due to total percentage less than 40")
# else:
#     print("You are pass")

# text = input("enter the text:- ")

# if ("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if spam:
#     print("This text is spam")
# else:
#     print("This text is not a spam")

# username = input("enter your user name:- ")

# if len(username) <= 10:
#     print("Plz enter min 10 char")
# else:
#     print(f"Your userName:- {username}")

# list1 = [10,20,30,40]
# ko = int(input("enter you fav digit:- "))

# if ko in list1:
#     print("You digit in list")
# else:
#     print("NO")

str1 = input("Enter your text:- ")

aayush = "Aayush","AAYUSH","AaYuSh"

if str1 in aayush:
    print("YES")
else:
    print("NO")