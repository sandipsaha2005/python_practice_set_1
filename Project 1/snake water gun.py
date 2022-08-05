import random
def wingame(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
    elif you=="g":
        return True

        
    elif comp=="w":
        if you=="g":
            return False
    elif you=="s":
        return True

    elif comp=="g":
        if you=="s":
            return False
    elif you=="w":
        return True

print("computer turn: snake(s) water(w) gun(g)")
randomno=random.randint(1,3)
if randomno==1:
    comp="s"
if randomno==2:
    comp="w"
if randomno==3:
    comp="g"

you=input("your turn: snake(s) water(w) gun(g)")
a=wingame(comp,you)
print(f"comp chose {comp}")
print(f"your chose {you}")

if a ==None:
    print("the game is tie")
elif a==True:
    print("you win the game")
else:
    print("you loose")




