# # def fac(n):
# #     if n == 0 or  n == 1:
# #         return 1
# #     return n * fac (n-1)

# # aa = fac(5)
# # print(aa)

# # def max(num1,num2,num3):
# #     if num1 > num2:
# #         if num1 > num3:
# #             return num1
# #         else:
# #             return num3
# #     else:
# #         if num2 > num3:
# #             return num2
# #         else:
# #             return num3
    
# # a = max(10,1,3)
# # print(a)

# # def ferh(cel):
# #     return (cel*(9/5))+32

# # c = 45
# # f = ferh(c)
# # print(f)




# n = 3
# for i in range(n):
#     print("*" * (n-i))



# def sum(n):
#     if n == 1 or n == 0:
#         return 1
#     return n + sum(n-1)
# f = sum(10)
# print(f)

# n = 3
# for i in range(n):
#     print("*" * (n-i))

# def inch(n):
#     if n == 0:
#         return 0
#     return n *2.54
# gg = inch(2)
# print(gg,"cm")

# def remov(sp,word):
#     new = sp.replace(word," p")
#     return new.strip()
# ll = "i am aayush patel"
# nn = remov(ll,"aayush")
# print(nn)



def print_table(num):
    for i in range(1,11):
        print(num,'x',i,'=',num*i)
n = int(input())
print_table(n)