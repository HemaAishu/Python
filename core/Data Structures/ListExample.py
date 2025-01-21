# Accessing List :Indexing & Slicing
alphanum=[1,2,"sara",5.62]
listOfList=[[1,2,3,4],['sara','murthy','24']]
print(alphanum) #Output : [1, 2, 'sara', 5.62]
print(listOfList) #Output : [[1, 2, 3, 4], ['sara', 'murthy', '24']]
print(listOfList[0]) #Output : [1, 2, 3, 4]
print(listOfList[0][0]) #Output : 1
print(alphanum[1:4]) #Output : [2, 'sara', 5.62]
print(alphanum[:2]) #Output : [1, 2]
print(alphanum[3:]) #Output : [5.62]