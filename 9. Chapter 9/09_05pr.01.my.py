#write a proram to read the text from a given file "poem.txt" and find out wheather it contains the word 'twinkle'
f=open('poem.txt')
t=f.read()
if 'twinkle' in t:
    print("twinkle is present in the poem")
else:
    print("this word is not in that file")
f.close()


# another try
g=open('poem.txt')
t=g.read()
if "twinkle" in t:
    print("the word twinkle is present in the file")
    
else:
    print("the word is not in that file")
g.close()



