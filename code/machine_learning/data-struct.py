#Tuple
a = (1, 2, 3) 
print (a)
#List
mylist = [1, 2, 3] 
print(f"Zeroth Value: {mylist[0]}")
mylist.append(4) 
print(f"List Length: {len(mylist)}")
for value in mylist: 
    print (value)

#Dictionary
mydict = {'a': 1, 'b': 2, 'c': 3} 
print(f"A value: {mydict['a']}")
mydict['a'] = 11 
print(f"A value: {mydict['a']}")
print(f"Keys: {mydict.keys()}")
print(f"Values: {mydict.values()}")
for key in mydict.keys(): 
    print (mydict[key])