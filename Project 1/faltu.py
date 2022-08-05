from operator import truediv
import random
from re import L
def wingame(comp,you):
    if comp==you:
        return None
    elif comp== "snake":
        if you=="water":
            return False
        elif you=="gun":
            return True
        
    
    elif comp== "water":
        if you=="gun":
            return False
        elif you=="snake":
            return True
        

    
    elif comp== "gun":
        if you=="snake":
            return False
        elif you=="water":
            return True
print("comp turn: snake water gun?")
randomno=random.randint(1,3)
if randomno==1:
    comp="snake"
if randomno==2:
    comp="water"
if randomno==3:
    comp="gun"
you=input("your turn: snake water gun?")
a=wingame(comp,you)
print(f"computers turn {comp}  ")
print(f"your turn     {you}  ")
if a==None:
    print("the game is tie")
elif a==True:
    print("you won the game!")
else:
    ("you lost the game") 






        

