   # Inheritences
   
class Animal:
    
    def sound(self):
        print("Animal make a sound...!");
        
class Dog(Animal):
    
    def bark(self):
        print("Dog say worl! worl!...");
        
        
dog = Dog();
dog.sound();
dog.bark();