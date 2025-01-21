def checkage(age):
    return "Adult" if age >18 else "Minor"


class Person:
    def __init__(self,name,age,location):
        self.name=name
        self.age=age
        self.location=location

    def __str__(self):
        return f"Name: {self.name} , Age: {self.age}, Location: {self.location}"

    def introduce(self):
        return f" Hello , My name is {self.name}, I live in {self.location} and i am an {checkage(self.age)}"


# person=Person("Sara",20,"Bengaluru")
# print(person)
# print(person.introduce())