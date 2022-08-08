# # a = ['hii', 'how', 'are', 'you']
# # # [['i':2],['o':1],['a':1,'e':1],['o':1,'u':1]]

# # main = []
# # for i in a:
# #     w = []
# #     for j in i:
# #         if j in 'aeiou':
# #             if j not in w:
# #                 count = i.count(j)
# #                 w.append(j)
# #                 w.append(count)
# #     main.append(w)
# # print(main)


#  Q1>>> [6,9,8,7,4,2] :- even : odd; odd as it is

# a = [6,9,8,7,4,2]

# for i in range(0,6):
#     if i % 2 == 0:
#         print(a[i]+1)
#     else:
#         print(a[i])

# Q2>>> ['hii','how','are','you']
#       [['i',2],['o',1],['a',1,'e',1],['o',1,'u',1]]  
# a =  ['hii','how','are','you']
# main = []
# for i in a:
#     w = []
#     for j in i:
#         if j in 'aeiou':
#             if j not in w:
#                 count = i.count(j)
#                 w.append(j)
#                 w.append(count)
#     main.append(w)
# print(main)

print()
print("Chole Bhature For Press-a And Price Is 150RS")
print("Veg Sandwich For Press-b And Price Is 100RS")
print("Bread Butter For Press-c And Price Is 70RS")
print("Veg Toast For Press-d And Price Is 80RS")
print("Special Pav Bhaji For Press-e And Price Is 200RS")

a = "Chole Bhature And Price Is 150RS"
b = "Veg Sandwich And Price Is 100RS"
c = "Bread Butter And Price Is 70RS"
d = "Veg Toast And Price Is 80RS"
e = "Special Pav Bhaji Price Is 200RS"
print()

chloe_bhature =  150
Veg_Sandwich = 100
Bread_Butter = 70
Veg_Toast = 80
Special_Pav_Bhaji = 200


user_order = input("Enter Your Order:- ")

if user_order == "a" or user_order == "A":
    print()
    print(f"Your Order {a}")

elif user_order == "b" or user_order == "B":
    print()
    print(f"Your Order {b}")

elif user_order == "c" or user_order == "C":
    print()
    print(f"Your Order {c}")

elif user_order == "d" or user_order == "D":
    print()
    print(f"Your Order is {d}")

elif user_order == "e" or user_order == "E":
    print()
    print(f"Your Order {e}")

else:
    print()
    print("Please Enter Valid Order")

print()

student = input("Are You Student:- ")

print()
print(end="               ""Iteam No")
print(end="     ""Iteam Name")
print(end="     ""amount")
