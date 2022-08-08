#Write a program to make a copy of a text file “this.txt.”
with open("9. Chapter 9\\this.txt") as f:
    content=f.read()
with open("akshay.txt","w") as f:
    f.write(content)
