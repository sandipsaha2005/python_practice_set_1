# for i in range(2,21):
#     with open(f"the multiplication of {i}","w") as f:
#         for j in range(1,11):
#             f.write(f"{i} X {j}={i*j}\n")


# import os.path

# save_path = 'D:\\python\\program\\9. Chapter 9\\tables.py\\good'

# name_of_file = input("What is the name of the file: ")

# completeName = os.path.join(save_path, name_of_file+".txt")         

# file1 = open(completeName, "w")

# toFile = input("Write what you want into the field")

# file1.write(toFile)

# file1.close()


for i in range(2,21):
    with open(f"tables1/good/the multiplication table of {i}","w") as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")
