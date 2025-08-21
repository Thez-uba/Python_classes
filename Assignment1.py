# Parent class
class Animal:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def sound(self):
        return("This animal makes a sound.")

# Child class: Dog
class Dog(Animal):
    def sound(self):
        return(f"{self.name} the dog barks.")

# Child class: Cat
class Cat(Animal):
    def sound(self):
        return(f"{self.name} the cat meows.")

# Child class: Lion
class Lion(Animal):
    def sound(self):
        return(f"{self.name} the lion roars.")

# Instantiating objects
dog = Dog("Chelsea", "Labrador", 3)
cat = Cat("Caroline", "Siamese", 2)
lion = Lion("Missy", "African Lion", 5)

Animals = [dog, cat, lion]
for animal in Animals:
    print(f"{animal.name} makes a sound:{animal.sound()}")

# Accessing the Methods
dog.sound()   # Output: Chelsea the dog barks. 
cat.sound()   # Output: Caroline the cat meows. 
lion.sound()  # Output: Missy the lion roars. 
