#oops 

# class Student():
#     FormName = "Data For Student Id"
#     def printdata(self):
#         print(f"Student Name {self.name}")
#         print(f"Student Rool No Is {self.roolnumber}")

# data = Student()
# data.name = "Aayush"
# data.roolnumber = "31"
# data.printdata()

# class Company():
#     name ="InfoTech"

# aayush = Company()
# aayush.name
# Company.name = "InfoGaming"
# print(aayush.name)

# class Empol:
#     company = "Google"
#     salery = "100k"
# aayush = Empol()
# aayush.company = "YouTube"
# aayush.salery = 100000
# print(aayush.company)
# print(aayush.salery)

# class selfm:
#     company = "Google"
#     def gets(self):
#         print(f"Salary is {self.salary}")
# aayush = selfm()
# aayush.salary = 10200
# aayush.gets()
# # upr self vadu ne niche aayush varu same j che 
# class selfm:
#     company = "Google"
#     def gets(aayush):
#         print(f"Salary is {aayush.salary}")
# aayush = selfm()
# aayush.salary = 10200
# aayush.gets()

#staticmethod  atle aapre j function ma self lakyi che a na lakye to pan chale
# class staticmethodm:
#     @staticmethod
#     def aayu():
#         print("hello")

# aayush = staticmethodm()
# aayush.aayu()


# constructor

# class ABC:
#     company = "ABC"

#     def __init__(self,name,salary,service):
#         self.name = name
#         self.salary = salary
#         self.service = service

#     def printdata(self):
#         print(f"name is {self.name}")
#         print(f"salary is {self.salary}")
#         print(f"service is {self.service}")

# aayush = ABC("Aayush",100000,"Python")
# aayush.printdata()


# class Programmer:
#     company = "Microsoft"

#     def __init__(self,name,products):
#         self.name=name
#         self.products=products

#     def getdata(self):
#         print(f"The name of programmer is {self.name} and the product is {self.products}")

# aayush = Programmer("Aayush","Skype")
# ashutosh = Programmer("Ashutosh","GitHub")
# aayush.getdata()
# ashutosh.getdata()

# class Cal:
#     def __init__(self,num):
#         self.number = num
    
#     def squre(self):
#         print(f"The value of {self.number} squre is {self.number **2}")
    
#     def squreroot(self):
#         print(f"The value of {self.number} squreroot is {self.number **0.5}")
    
#     def cube(self):
#         print(f"The value {self.number} cube is {self.number **3}")

# a = Cal(3)
# a.squre()
# a.squreroot()
# a.cube()



# class Sample:
#     a = "Aayush"

# obj = Sample()
# obj.a = "Ashutosh"
# '''
# sample.a ma aayush j print karshe becuse a class no a che ne obj.a che a obj no che atle ema ashutosh j print karshe. 
# '''
# # Sample.a = "Ashutosh" ne aavu karshu to bane ma Ashutosh j print karshe
# print(Sample.a)
# print(obj.a)


class Train:

    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getinfo(self):
        print()
        print("**************************************************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
    
    def fareInfo(self):
        print(f"The price of the ticket is Rs.{self.fare}")
        print("**************************************************")
    
    def bookTickets(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry this train is full!")
    
check = Train("Rajdhani Express : 14015",100,300)
check.getinfo()
check.bookTickets()
check.fareInfo()
check.getinfo()