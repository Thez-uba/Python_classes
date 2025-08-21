# Class
# Object
# Method Overriding
# Method Overloading
# Encapsulation
#Abtraction
#Polymorphism

# Class
class MyFirstClass:
    x= 98
    name="Thelma"
    def method1():
        print("Welcome to OOP class")

# Creating object from a class... Instantiating
obj1= MyFirstClass()
obj2= MyFirstClass()

#Accessing obj attributes
print(obj1.x)
print(obj1.name)

#Accessimg method
obj2.method1()

class MyFirstClass1:
    def __init__(self):
        self.a=98
        self.name="Thelma"
    def method1(self):
        print("Welcome to OOP class")

object1= MyFirstClass1()
object1.method1()

# Using Parameters
class MyFirstClass2:
    def __init__(self, number, username):
        self.a= number
        self.name=username
    def method1(self):
        print("Welcome to OOP class")

object2= MyFirstClass2(98,"Mike")
object2.method1()
object3= MyFirstClass2(56,"Vicky")

# Inheritance
class Shape:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
# Child class
class Square(Shape):
    def __init__(self, name, width, height, diameter):
        super().__init__(name, width, height)
        self.diameter = diameter

    def area(self):
        print(f"{self.width**2}")

# Class for Rectangle
class Rectangle(Shape):
    pass

# Instantiating square...(Child)
sqr1 = Square("Square",  45, 45, "456cm")
print(sqr1.name)
sqr1.area()

# Intantiating Rectangle Object
rect1 = Rectangle("Recatngle", 34, 23)

# Abstraction
class coffeeMachine:
    def __init__(self, water_qnt, tea_qnt):
        self.water_qnt = water_qnt
        self.tea_qnt = tea_qnt

    def makeCoffee(self):
        # boil water
        self.__boilWater()

        # brew coffee
        self.__brewCoffee()
    
    # Method to boil water.... To hide under makeCoffee using __ to name
    def __boilWater(self):
        print("Water is boiling at 296deg...")

    def __brewCoffee(self):
        print("I am brewing coffee...")

# Instantiating coffee machine
machine1 = coffeeMachine("23cm", "15cm")
machine1.makeCoffee()
# machine1.__boilWater()... cannot be accessed.

# Encapsulation... Hiding data, binding to the parent..
# class Shapes:
#     def __init__(self, name, width, height):
#         self._name = name # Uses _
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
    
# # Child class
# class Squares(Shapes):
#     def __init__(self, name, width, height, diameter):
#         super().__init__(name, width, height)
#         self.diameter = diameter

#     def area(self):
#         print(f"{self.width**2}")

# # Class for Rectangle
# class Rectangles(Shapes):
#     pass

# # Instantiating square...(Child)
# sqr1 = Squares("Square",  45, 45, "456cm")
# print(sqr1.name)
# sqr1.area()

# # Intantiating Rectangle Object
# rect1 = Rectangles("Recatngle", 34, 23)

# Polymorphism
text = "This is to demonstrate polymorphism in python"
fruits = ["Orage", "Mango", "Banana", "Apple"]
car = {
    "brand": "Ford",
    "model": "Mustang",
    "yea": 1964
}

# Use the len() function to get the length of different data types
objts = [text, fruits, car]
for obj in objts:
    print(f"the length of {obj} is {len(obj)}")