class Mammal:
    def walk(self):
        print("walk")


class Dog:
    def walk(self):
        print("walk")


# Let's say you want to add a walk method to the cat class. Instead of repeating code you can use inheritance.
# You don't have to repeat code.
# DRY Don't Repeat Yourself

class Cat: # Not good...
      def walk(self):
        print("walk")


class Dog(Mammal): # Dog class inherits all methods from Mammal class.
    pass # Prevents an empty class.


class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.walk()

# The overall Mammals class has methods you would want all mammals to do...
# You can still add methods individually to Dog and Cat classes such as bark and meow as they make diff noises.