mydict={
    "fast": "in quick mannar",
   "sandip": "coding learner",
   "marks": [1,2,3],
   "anotherdict": {'sandip': 'player'},
   1:  2
   }

 print(type(mydict.keys()))
 print(list(mydict.keys()))
 print(mydict.keys())# to print the keys ....
 print(mydict.values())# to print the key  values ....
 print(mydict.items())  #toprint all cotants from the dictionary...

print(mydict)
updateddict= {  "lovish" : "friend",
"sandip": "students",
"anushree" : "friend"
}
mydict.update(updateddict)
print(mydict)

print(mydict.get("anushree"))  # if  the oblect is not in the dictionary it will throw none as the result.
print(mydict["anushree"])  # if the oblect is not in the dictionary it will throw error as the result..
 
#wrong
print(mydict.get("anushree2")) # it will give you none as the result...
print(mydict("anushree2"))   # it will give you error as the result of my code ...












