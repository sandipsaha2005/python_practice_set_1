# #Write a program to find greatest of four numbers entered by the user.

n1=int(input("enter the firs number \n"))
n2=int(input("enter the second number\n"))
n3=int(input("enter the third number\n"))
n4=int(input("enter the fourth number\n"))

if(n1>n4):
    f1=n1
else:
    f1=n4
if(n2>n3):
    f2=n2
else:
    f2=n3

if(f1>f2):
    print(str(f1) +" is greatest one")
else:
    print(str(f2) +" is greatest one" )

































