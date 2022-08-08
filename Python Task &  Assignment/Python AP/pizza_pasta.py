


show_menu = [
    ["1. large pizza = 10.99 AUD "], 
    ["2. large Pizzas = 20.99 AUD"],
    ["3. Large Pizzas = 29.99 AUD"],
    [" ***Buy 4 or more pizza and get 1.5lt of soft drink free***"],

["1. large pasta = 9.5 AUD "],

["2. large pastas = 17.00 AUD "],

["3. large pastas = 27.50 AUD"],

["***Buy 4 or more pastas and get 2 bruschetta free.***"],

["***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free."],

]

for i in show_menu:
    print(i)


name = input("Enter Your Name:- ")

print("Welcome ,",name)

pizza_order = int(input("Enter number or pizza order you want :- "))
pizza_order_total = pizza_order * 10.99
print(" your pizza order amount is :- ",pizza_order_total)


if pizza_order >= 4:
    print("*** Congratulations !! 1.5lt softdrink free *** ")

else:
    pass



pasta_order = int(input("Enter number or pasta order you want :- "))
pasta_order_total = pasta_order * 9.5
print("Your pasta order amount is :- ",pasta_order_total)

if pasta_order >= 4 :
    print("*** Congratulations !! get 2 bruschetta free ***")
    print("*** Congratulations !! get 2 chocco brownies ice cream free ***")

else:
    pass

print("Your Total Order Is :- ",pizza_order_total + pasta_order_total)


owner = pizza_order_total + pasta_order_total

print("Your Net order amount of the day is:- ", owner)

order_again = input("want to enter order from another customer (Y/N):- ")


if order_again == "Y":
        
    name = input("Enter Your Name:- ")

    print("Welcome ,",name)

    pizza_order = int(input("Enter number or pizza order you want :- "))
    print(" your pizza order amount is :- ",pizza_order*10.99)


    if pizza_order >= 4:
        print("*** Congratulations !! 1.5lt softdrink free *** ")

    else:
        pass



    pasta_order = int(input("Enter number or pasta order you want :- "))
    pasta_order_total = pasta_order * 9.5
    print("Your pasta order amount is :- ",pasta_order_total)

    if pasta_order >= 4 :
        print("*** Congratulations !! get 2 bruschetta free ***")
        print("*** Congratulations !! get 2 chocco brownies ice cream free ***")

    else:
        pass

    print("Your Total Order Is :- ",pizza_order_total + pasta_order_total)


    owner = pizza_order_total + pasta_order_total

    print("Your Net order amount of the day is:- ", owner)

else:
    print("Thnaks For Join Us")