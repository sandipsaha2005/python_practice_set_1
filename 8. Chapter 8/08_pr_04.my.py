#write a recursive function to calculate the sum of first natural number
def sum(n):
    if n==0:
        return 0

    else:
        convert= n*(n-1)/2
        return convert
a=int(input("enter the number"))
v=sum(a)
print(sum(a))



