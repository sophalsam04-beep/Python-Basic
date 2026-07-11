     # Constructor in python programing
         # Default constructor
class student:
    def __init__(self):
        print("Constructor called succesfully...!");
        
student = student();


     # Constructor with Parameter
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = person("Un virak",22);
p2 = person("chantha",18);
print(p1.name);
print(p2.name);

print(p1.age);
print(p2.age);



     # Methods in python
class banker:
    def __init__(self, name):
        self.name=name
        
    # Methods
    def display(self):
        print("Name : ", self.name);
        
        
        # Display full methods
b = banker("Sam sophal");
b.display();

   # Shorthand
print(b.name);


