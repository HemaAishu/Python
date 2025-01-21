a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b)) # Output : {1, 2, 3, 4, 5}
print(a.intersection(b)) # Output : {3}
print(a.difference(b)) # Output : {1, 2}
print(b.difference(a)) # Output : {4, 5}
print(a.symmetric_difference(b)) # Output : {1, 2, 4, 5}
print(a.isdisjoint(b)) # Output : False -> Return True if two sets have a null intersection.
print(a.issubset(b)) # Output : False
print(a.issuperset(b)) # Output :False
print(a.issuperset(a)) # Output :True