dict1={x: x*5 for x in range(1,6)}
print(dict1) # Output : {1: 5, 2: 10, 3: 15, 4: 20, 5: 25}

dict2={x if(x%2==0) else None for x in range(2,20)}
print(dict2) # Output : {None, 2, 4, 6, 8, 10, 12, 14, 16, 18}

dict3={x for x in range(1,20) if(x%2==0)}
print(dict3) # Output :{2, 4, 6, 8, 10, 12, 14, 16, 18}