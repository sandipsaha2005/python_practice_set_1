#Write a program to wipe out the contents of a file using python.
with open("akshay.txt") as f:
    a=f.read()
with open("akshay.txt","w") as f:
    a=f.write("")
    