def game(comp,you):
    if comp == you:
        return None
    elif comp == 'S':
        if you == 'W':
            return False
        elif you == 'G':
            return True
    elif comp == 'W':
        if you == 'G':
            return False
        elif you == 'S':
            return True
    elif comp == 'G':
        if you == 'S':
            return False
        elif you == 'W':
            return True

import random

print("Comp Turn: Snake(S) Water(W) or Gun(G)")
randno = random.randint(1,3)
if randno == 1:
    comp = "S"
elif randno == 2:
    comp = "W"
elif randno == 3:
    comp = "G"

you = input("Your Turn: Snake(S) Water(W) or Gun(G):- ")
a = game(comp,you)

print(f"Computer chose:- {comp}")
print(f"you chose:- {you}")

if a == None:
    print("The game is tie")
elif a:
    print("You Win")
else:
    print("You Lose")