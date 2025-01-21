with open("TxtWriting.txt", 'w') as file:
    text="Hai Hello , This is Python, Nice to meet You!!"
    res=file.write(text) # returns the lingth of string which is wriiten in the file
    print(res)
    if(res > 0):
        print("Successfully Written into the document")
    else:
        print("Nothing is written in the file")

with open("TxtWriting.txt", 'r') as file:
    content= file.read()
    print(content)