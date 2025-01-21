with open('Txtfile.txt', 'r') as file:
    for line in file:
        print(line)



with open('Txtfile.txt', 'w') as file:
    for num in range(1,11):
        file.write("Hello World {}\n".format(num))
