# n!=1*2*3*4*n

# n=9
# product=1
# for i in range(n):
#     i=i+1
#     product=product* (i)
#     print(product)






# def factorial_iter(n):
#     product=1 
#     for i in range(n):
#         i=i+1
#         product = product * (i)
#     return product


# a=factorial_iter(int(input("the number do want the factorial")))  
# print(a)


# #factorial with recursive
# def factorialrecursive(n):
#     if n==1:
#         return 1
#     else:
#         return n* factorialrecursive(n-1)
# what is happening in this line
# if n=5
# # 5* factorialrecursive(4)
# # 5*4 factorialrecursive(3)
# # 5*4*3 factorialrecursive(2)
# # 5*4*3*2 factorialrecursive(1)
# # 5*4*3*2*1=120
# a=int(input("enter the number "))
# g=factorialrecursive(a)
# print(g)







# def factorial_recursive(n):
#     if n==1 or n==0:
#         return 1
#     return n * factorial_recursive(n-1)


# a=factorial_recursive(int(input("Enter the number do you want to get the fctorial")))
# print(a)

#gandmara fobinacci

# def fibonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# v=int(input("enter the number "))
# a=fibonacci(v)
# print(a)




