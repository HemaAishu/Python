class Shape:
    def draw(self):
        print("Draw method by Shape")

class Cicle(Shape):
    def draw(self):
        print("Draw method by Circle")

class Rectangle(Shape):
    def draw(self):
        print("Draw method by Rectangle")

x=Cicle()
x.draw()