dict1= {'land':2563.85,"car":500000,"name":"Priya",1:156}
# Using Key
print(dict1['land']) # Output :2563.85
# print(dict1['address']) # KeyError: 'address'
#Using get() method
print(dict1.get("name")) # Output : Priya
print(dict1.get("address")) # Output : None

# Adding and Updating
dict2={1:'One',2:'Two',3:'Three',4:'IV'}
print(dict2) # Output : {1: 'One', 2: 'Two', 3: 'Three', 4: 'IV'}
# Adding new Key and Value in Existing Dictionary
dict2[5]="Five"
print(dict2) # Output : {1: 'One', 2: 'Two', 3: 'Three', 4: 'IV', 5: 'Five'}
#Updating the Existing Key's Value.
dict2[4]='Four'
print(dict2) # Output : {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

# Deleting
#Using key to remove
del dict2[3]
print(dict2)# Output :{1: 'One', 2: 'Two', 4: 'Four', 5: 'Five'}

#Usinng pop () method
delItem=dict2.pop(5)
print(delItem)# Output : Five
print(dict2)# Output :{1: 'One', 2: 'Two', 4: 'Four', 5: 'Five'}

# clear () Method
dict2.clear()
print(dict2)# Output : {}