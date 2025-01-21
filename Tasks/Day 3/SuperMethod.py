class Person:
    def __init__(self,name,age,location):
        self.name=name
        self.age=age
        self.location=location
        print("Constructor oF Person Class")
    def __str__(self):
        return f"Person: {self.name},{self.age},{self.location}"

class Student(Person):
    def __init__(self,name,age,location):
        super().__init__(name,age,location)
    def __str__(self):
       return f"Student :{self.name},{self.age},{self.location}"


x=Student("Sara",24,"Delhi")
print(x)