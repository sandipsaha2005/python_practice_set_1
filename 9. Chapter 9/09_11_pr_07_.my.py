#Write a program to find out the line number where python is present from question 6.
content=True
i=1
with open("9. Chapter 9\\log.my.txt") as f:
    while content:
        content=f.readline()
        if "python" in content.lower():
            print(content)
            print(f"yes python is present on line number {i}")
        i+=1






















