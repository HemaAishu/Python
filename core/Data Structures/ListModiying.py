# Adding Elements
myList=[1,2]
print(myList) #Output : [1, 2]
myList.append("sara")
print(myList) #Output : [1, 2, 'sara']
myList.extend(["priya",255])
print(myList) #Output : [1, 2, 'sara', 'priya', 255]
myList.insert(2,"Hema")
print(myList) #Output : [1, 2, 'Hema', 'sara', 'priya', 255]
print("*********************************************************************")

# Removing Element
myList2=[1, 2, 'Hema', 'sara', 'priya', 255,1]
print(myList2)#Output : [1, 2, 'Hema', 'sara', 'priya', 255, 1]
myList2.remove(1)
print(myList2)#Output : [2, 'Hema', 'sara', 'priya', 255, 1]
myList2.pop()
print(myList2)#Output : [2, 'Hema', 'sara', 'priya', 255]
myList2.pop(3)
print(myList2)#Output : [2, 'Hema', 'sara', 255]
myList2.clear()
print(myList2)#Output : []
print("*********************************************************************")

# Updating Elements:
myList3=[1, 2, 'Hema', 'sara', 'priya', 255,1]
print(myList3)#Output : [1, 2, 'Hema', 'sara', 'priya', 255, 1]
myList3[3]= "Ankitha"
print(myList3)#Output :[1, 2, 'Hema', 'Ankitha', 'priya', 255, 1]
