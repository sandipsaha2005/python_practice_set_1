# this program is in the chapter no 9.

for i in range(2,21):    
    with open(f"the multiplication table of {i}","w") as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")

    