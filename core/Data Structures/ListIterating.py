myList1=[1, 4, 8,24,25, 255,1]

for item in myList1:
    print(item)

squaree=[(x if (x %2 ==0 ) else 0)for x in myList1]
print(squaree) # Output : [0, 4, 8, 24, 0, 0, 0]
