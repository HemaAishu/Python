# Accessing :
tup= tuple([1,2,5,8,4,'Sara Murthy',True])
#Indexing
print(tup[0]) #Output : 1
print(tup[-5]) #Output : 5

# Slicing
print(tup[2:5]) #Output : (5, 8, 4)
print(tup[4:]) #Output : (4, 'Sara Murthy', True)
print(tup[:4]) #Output : (1, 2, 5, 8)
#Reverse Order
print(tup[::-1]) #Output : (True, 'Sara Murthy', 4, 8, 5, 2, 1)
#"start from the end and move backwards with a step of -2"
print(tup[::-2]) #Output : (True, 4, 5, 1)
#"start from the end and move backwards with a step of -3"
print(tup[::-3]) #Output : (True, 8, 1)
# start from the begining moves forward with 2 step
print(tup[::2]) #Output : (1, 5, 4, True)