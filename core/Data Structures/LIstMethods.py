listOfList=[1,2,3,4,1,2,"sara",5.62]
print(listOfList) # Output: [1, 2, 3, 4, 1, 2, 'sara', 5.62]

listOfList.append("Hema")
print(listOfList) # Output: [1, 2, 3, 4, 1, 2, 'sara', 5.62, 'Hema']

extendedList=[76.9,8787.01,"list"]
listOfList.extend(extendedList)
print(listOfList) # Output: [1, 2, 3, 4, 1, 2, 'sara', 5.62, 'Hema', 76.9, 8787.01, 'list']

print(f"Index of element \"sara\" if {listOfList.index("sara")}") # Output: Index of element "sara" if 6

print(f"count the frequency of 1 in {listOfList.count(1)}")
# listOfList.reverse()
# print(listOfList)
reversed=listOfList[::-1]
print(reversed)

for item in listOfList:
    print(item if isinstance(item,int) else "")
