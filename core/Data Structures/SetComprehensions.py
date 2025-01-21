set1={8,9,5,3,4,1,5,2,6,4,5,8}
for ele in set1:
    print(ele)  # Output : 8 9 5 3 4 1 5 2 6 4 5 8

# Set Comprehensions
squared_set = {x**2 for x in range(5)}
print(squared_set)  # Output : {0, 1, 4, 9, 16}

# Nested Sets
nested_set = {frozenset({1, 2}), frozenset({3, 4})}
print(nested_set)  # Output: {frozenset({1, 2}), frozenset({3, 4})}
