# Same Type
dict3={1:"ganesh",2:"abi",3:"sara",4:"anu"}
print(dict3) # Output : {1: 'ganesh', 2: 'abi', 3: 'sara', 4: 'anu'}
# Different Data Type
dict1= {"land":2563.85,"car":500000,"name":"Priya"}
print(dict1) # Output : {'land': 2563.85, 'car': 500000, 'name': 'Priya'}
# Using constructor
dict2 = dict(name="anu",age=24,loc="bengaluru")
print(dict2) # Output : {'name': 'anu', 'age': 24, 'loc': 'bengaluru'}
# Empty Dictionery
dict3={}
print(dict3) # Output : {}
print(type(dict3)) # Output : <class 'dict'>

# List Of Tuples
dict4 = dict([("name", "Alice"), ("age", 25)])
print(dict4["name"]) # Output : Alice