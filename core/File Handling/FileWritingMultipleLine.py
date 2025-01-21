list=["Hello World","How are you ?","What is your name?","Nice to meet you!!"]
with open("TxtWriteMultiple.txt", 'w') as file:
    file.writelines(list)

with open("TxtWriteMultiple.txt", 'r') as file:
    content=file.read()
    print(content) # Output : Hello WorlHow are you ?What is your name?Nice to meet you!!

with open("TxtWriteMultiple.txt", 'w') as file:
    for line in list:   #The print() function automatically appends a newline character (\n) at the end of each line when writing to the file.
        print(line,file=file) #The file=file argument specifies the file where the output should be written.

with open("TxtWriteMultiple.txt", 'r') as file:
    content=file.read()
    print(content)
    # Output :
    # Hello World
    # How are you ?
    # What is your name?
    # Nice to meet you!!