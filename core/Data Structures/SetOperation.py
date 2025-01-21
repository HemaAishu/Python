set1={8,9,5,3,4,1,5,2,6,4,5,8}
print(set1) # Output : {1, 2, 3, 4, 5, 6, 8, 9}

# Adding the element
set1.add(100)
print(set1) # Output : {1, 2, 3, 4, 5, 6, 100, 8, 9}

# Removing Element
# Using remove() method
# set1.remove(101) #KeyError: 101
print(set1) # Output : {1, 2, 3, 4, 5, 6, 100, 9}

# Using discard() method
set1.discard(101)
print(set1) # Output :{2, 3, 4, 5, 6, 100, 8, 9}

# Using pop() method
set1.pop()
print(set1) # Output :{2, 3, 4, 5, 6, 100, 8, 9}
