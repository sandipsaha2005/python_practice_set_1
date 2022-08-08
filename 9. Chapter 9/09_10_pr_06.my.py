#Write a program to mine a log file and find out whether it contains ‘python’.
with open("9. Chapter 9\\log.my.txt") as f:
    content = f.read()
if 'Python ' in content:
    print("yes python is present in the log file")    
else:
    print("no there is no python present in the log file")
