#write a python function to remove a given word from a list and strip it at the same time
def string_strip(string,word):
    newStr= string.replace(word,"")
    return newStr.strip()
this="sandip                is a good boy"
n=string_strip(this,"sandip")
print(n)
