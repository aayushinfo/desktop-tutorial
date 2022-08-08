# # mydict = {
# #     "aayush" : "A coder",
# #     "Pinto" : "Unlimited trick",
# #     "darshan" : "Fatuu",
# #     1 : "ajs"
# # }
# # print(mydict.keys())
# # print(mydict.values())
# # print(mydict.items())
# # print(mydict)
# # update = {
# #     "anil" : "vimal"
# # }
# # mydict.update(update)
# # print(mydict)
# # print(mydict.get("aayush"))
# # print(mydict["aayush"]) # upr get varu ane aa line varu bane same j che pan aapre jo mydict aayush che ne aayush 2 laki deshu to aa line error aapshe pan get none print karshe.

# # set : set is a collection of non repetitve elements . matlb k aapre a = {1,2,3,4,1} aapyu to aa khali 1,2,3,4 j print karshe last ma j 1 che a print na kre matlb k set ek value ne ek j var print karshe

# # a ={1,2,3,4,1}
# # print(a)

# a = {}
# print(type(a)) # aa empty dict che
# b = set()
# print(type(b)) # aa empty set che
# b.add(6) # add che a empty set ma value add karshe
# b.add(8)
# # b.add([4,5,6]) # aapre set ni andr list na add kari shkaye karn ke list a change karie shakya che
# b.add((4,5,6)) # aapre set ni andr tuple ne add kari shakye che tuple change na thya atle
# # b.add({4,5,6}) # aapre set ni andr dict na add kari shkaye karn ke dict a change karie shakya che
# print(b)
# print(len(b))
# b.remove(6)
# print(b)
# print(b.pop()) # random value delte kari deshe
# print(b)
# print(b.clear())

# hi = {
#         "pankha" : "fan",
#         "dabba" : "Box ",
#         "vastu" : "item"
# }
# print("option are",hi.keys())
# a = input("Enter the hindi word")
# # print("Your word mining is:- ",hi[a])
# print("Your word mining is:- ",hi.get(a))

# n1 = int(input("enter number 1:- "))
# n2 = int(input("enter number 2:- "))
# n3 = int(input("enter number 3:- "))
# n4 = int(input("enter number 4:- "))
# n5 = int(input("enter number 5:- "))
# n6 = int(input("enter number 6:- "))
# n7 = int(input("enter number 7:- "))
# n8 = int(input("enter number 8:- "))

# set1 = {n1,n2,n3,n4,n5,n6,n7,n8}
# print(set1)

# ss = {20,20.2,"20"}  # jo 20.2 ni jagya a 20.0 hot to len 2 aavti pan 20.2 che atle 3 aave che 20 and 20.0 ni value sam hot atle len 2 aave 
# print(len(ss))

fav = {}
a = input("enter your fav lan aayush:-")
b = input("enter your fav lan pinto:-")
c = input("enter your fav lan henil:-")
d = input("enter your fav lan darshil:-")

fav["aayush"] = a
fav["pinto"] = b
fav["henil"] = c
fav ["darshil"] = d
print(fav)