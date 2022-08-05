def inchtocm(n):
    if n==0:
        return 0
    else:
        return n*2.54
#write a python function to convert inchs into cm
a=int(input("enter the number to convert into centemeter"))
g=inchtocm(a)
print(g)


#centemeter to inch
def cmtoinch(b):
    if b==0:
        return 0
    else:
        return b/2.54

a=int(input("eneter the number to convert into inch"))
v=cmtoinch(a)
print(v)