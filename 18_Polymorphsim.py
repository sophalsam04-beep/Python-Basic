   # Polymorphsims
class Dog:
    def sound(self):
        print("Dog say : Worl! Worl...!");
    
class Cat:
    def sound(self):
        print("Cat say Meow! Meow...!");
        
        
animals = [Dog(), Cat()];

for animal in animals:
    animal.sound();