# Numbers Strings Booleans
# Lists Dictionaries

numbers = [1, 2, 3]

# Pascal naming convention for classes.
# Objects are an instance of a class.
# Classes are used to define new types and have methods in the body of the class.
# A constructor is a function that gets called when creating an object.

class Point:
    def __init__(self, x, y): # constructor
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point(10, 20)
point1.draw()

point = Point(10, 20)
print(point.x)

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}.")

john = Person("John Smith")
print(john.name)
john.talk()

bob = Person("Bob Smith")
bob.talk()

# Each object is a different instance of a person class.



    
