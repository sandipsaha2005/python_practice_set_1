# for i in range(2,21):
#     with open(f"the multiplication of {i}","w") as f:
#         for j in range(1,11):
#             f.write(f"{i} X {j}={i*j}\n")



for i in range(2,21):
    with open(f"tables1/good/the multiplication table of {i}","w") as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")
