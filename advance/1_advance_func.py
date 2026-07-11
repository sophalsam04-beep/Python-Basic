    # 1. Default Argunments
def greet(name="Guest"):
    print("name : ", name);

greet("Sam Sophal");
greet();    


def car(name = "Mazda"):
    print("Name : ", name);

car("Toyota");
car();

      # 2. Keyword Argunment
def student(name, age):
    print("Name : ", name);
    print("Age : ", age);
    
student(name = "Un virak", age=22);


   # 3. Abtritary Argunments
def total(*number):
    print(number);
    print(sum(number));
    
total(10,20,30,40);



   # 4. Keyword Atritary Argunments
def profile(**info):
    for key, value in info.items():
        print(key, ":",value);
        
profile(name = "Un virak", age = 22, city = "Phnom Penh");


def people(**information):
    for key, value in information.items():
        print(key, ":", value);
        
profile(name = "Sophal", age = 22, city = "Phnom Penh");


    # Lambda expression
# lambda argunment : expression
square = lambda x: x**2;
print(square(5));

add = lambda a,b : a+b;
print(add(4,3));

