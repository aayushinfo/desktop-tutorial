# To add number
a = int(input("enter first number:- "))
b = int(input("enter second number:- "))

print("Sum is:-",a+b)

# For factorial of a number

a = int(input("enter a number:- "))
fac = 1

if a < 0:
     print("Factorial does not exit")
elif a == 0:
     print("Factorial is 0")
else:
     for i in range(1,a+1):
         fac = fac * i
     print(fac)
    # For Simple interest
a = int(input("enter principal amount:-"))
b = int(input("enter time period:- "))
c = int(input("enter rate of interest:-"))
d = (a*b*c)/100
print("interest is:-",d)


class myclass:
    x = 0
    def __init__(self,x):
        self.x=x
    def my_method(self):
        print("x:",self.x)
    def oddeven(self):
        if self.x%2==0:
            print(self.x,"is even number")
        else:
            print(self.x,"is odd number")
x = int(input("enter the value:-"))

a=myclass(x)
a.my_method()
a.oddeven()




a = ('ap',['jk','kl',])
a[1].pop()
print(a)





