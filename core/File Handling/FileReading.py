with open("TxtReading.txt", 'r') as file:
    for line in file:
        print(line.strip())

with open("TxtReading.txt", 'r') as file:
    content=file.read()
    print(content)

with open("TxtReading.txt", 'r') as file:
    for line in file:
        print(line.strip()) # Strip removes trailing newline characters