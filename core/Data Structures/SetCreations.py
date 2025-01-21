#set
set1={1,211,3,100,5,6,0,}
print(set1) # Output : {0, 1, 3, 100, 5, 6, 211}
# Using set constructor
set2=set({100,"Sara",253.62})
set2.add("Arun")
print(set2) # Output : {'Sara', 100, 253.62, 'Arun'}
#Frozen Set :
set3=frozenset({"abi","anu"})
# set3.add("Arun") # AttributeError: 'frozenset' object has no attribute 'add'
print(set3) # Output : frozenset({'abi', 'anu'})
# Empty Set
set4=set() # we can create empty set using set constructor
print(type(set4)) # Output : <class 'set'>
set5={}
print(type(set5)) # Output : <class 'dict'>