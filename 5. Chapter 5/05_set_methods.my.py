# creating an empty set..
b=set(   )
print(b)
#adding valus to an empty set.

b.add(5  )
b.add( 6 )
b.add((1,2,3 ))#  we can add tuples during adding values in the set...
b.add( 8 )
b.add( 7 )
b.add(3  )
b.add( 4 )  # we can't add any kind of list and dictionary during adding values in the set.....
b.add( 2 )
b.add(  1)
b.add(0  )   # ading repeted values can't change the set...
print(b)



#lenth of the set
print(len(b))    # prints the lenth of the set
b.remove(5)  # you can remove the item which is already in the set..
print(b)

b.pop()    # it will reomve any of this item from the set..
print(b)   




