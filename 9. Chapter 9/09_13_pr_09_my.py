#Write a program to find out whether a file is identical and matches the content of another file.
file1="9. Chapter 9\\this.txt"
file2="akshay.txt"

with open(file1) as f:
    f1=f.read()


with open(file2) as f:
    f2=f.read()

if f1==f2:
    print("these two files are identical. ")   
else:
    print("these two files are not identical")







