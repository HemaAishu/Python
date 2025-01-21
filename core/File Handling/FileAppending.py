with open("TxtAppending.txt", 'a') as appendFile:
    string ="Hello World!!\n"
    appendFile.write(string)
    print("Successfully Appended")

with open("TxtAppending.txt", 'r') as file:
    content=file.read()
    print(content)