



from random import Random, random
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

print("comp turn: snake(s) water(w) gun(g)?")
randomno=random.randint(1,3)
if randomno==1:
    comp="s"
elif randomno==2:
    comp="w"
elif randomno==3:
    comp="g" 

you =input("your turn: snake(s) water(w) gun(g)" ) 
a=wingame(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you}")

if a == None:
    print("the game is tie")
elif a==True:
    print("you win")
else:
    print("you loose")



   

        