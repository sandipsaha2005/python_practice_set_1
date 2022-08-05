#A spam comment is defined as a text contaning following keywords: 
'''"make a lot of money", "buy now", "click this", write a program to detect these 
spam programs '''


text=input("enter the text")
spam= False
  
if("make a lot of money" in text):
    spam= True
elif("buy now" in text):
   spam= True
elif("kbc" in text):
   spam= True
elif("suscribe now " in text):
   spam= True
else:
   spam=False 

if(spam):
   print("this text is spam")
else:
   print("this text is not a spam")






     





















