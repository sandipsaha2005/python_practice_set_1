from operator import truediv
import random
def wingame(comp,you):
    if comp==you:
        return None
    elif comp=="r":
        if you =="p":
            return True
        elif you=="s":
            return False

            
    elif comp=="p":
        if you =="s":
            return True
    elif you=="r":
        return False

    elif comp=="s":
        if you =="p":
            return False
    elif you=="r":
        return True

print("computer turn:rock(r) paper(p) sciser(s)")
randomno=random.randint(False,3)
if randomno==False:
    comp="r"
if randomno==None:
    comp="p"
if randomno==3:
    comp="s"
you=input("your turn:rock(r) paper(p) sciser(s)")
a= wingame(comp,you)
print(f"comp turn {comp}")
print(f"your turn {you}")


if a==None:
    print("the game is tie")
elif a==True:
    print("you won") 
else:
    print("you loose")


