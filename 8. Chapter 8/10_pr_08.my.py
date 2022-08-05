# make a multiplication table using function in python

# a=int(input("enter the number"))
# for i in range(10):
#     i=i+1
#     print(a*i)

def multiplicationtable(n):
  
    for i in range(1,11):
        print(n*i)
        
n=int(input("enter the nunber"))
g=multiplicationtable(n)
