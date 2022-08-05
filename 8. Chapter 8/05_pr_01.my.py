#write a python program to find the greatest of three numbers.



# def maximum(num1,num2,num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
            

#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3

# m=maximum(11,9,8)
# print(m)


def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
             return num3
        
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m=maximum(21,65,45)
print("the maximum number of thease numbers is ", + m)
print(type(m))


            
        















