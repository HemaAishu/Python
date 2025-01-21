from PersonClass import Person
class Employee(Person):
        def __init__(self, name, age, location):
                super().__init__(name, age, location)


x = Employee("Abi",15,"Chennai")
print(x.introduce())