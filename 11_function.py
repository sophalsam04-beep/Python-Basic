   # Function in python Programing
        # Function without Parameter
def Hello():
    print("Hello world");
    
Hello()


    # Function with parameter
def add(a,b):
    return (a+b);

result = add(12,3);
print(result);
def Greet(name):
    print("Name : ",name);

Greet("Vanda");


   # Function with Return values
def sub(x,y):
    return (x-y);

result_1 = sub(3,-5);
print(result_1);


  # Function with Default Parameter
def Hello(name = "Vanda"):
    print("Hello : ", name);
    
Hello();
Hello("Sam Sophal");
    
    

    # Function with Multiple value
def caculated(a,b):
    return a+b, a-b


sum_result, sub_result = caculated(4,9);
print("Sum result : ",sum_result);
print("Sub result : ",sub_result);



     # Arbitrary number of Argunments
     
def number(*args):
    return sum(args);

print(number(1,3,5,3,5));


def total(*number):
    print(sum(number));
    
total(10,30);
total(4,3,2,5,8);



    # Keyword Argunments
def students(**info):
    print(info);
    
students(name = "Vanda", age = "22", country = "Cambodia");



     # Lambda Functions syntax : lambda: argunment : expression
     
square = lambda x: x * x;
print(square(5));

def square(y):
    return y*y;

print(square(5));

add = lambda x,y: x+y;
print(add(3,5));

is_even = lambda x: x % 2 == 0;
print(is_even(30));
print(is_even(7));


    # Sort a list
students = [
    ("Sam sophal", 85),
    ("Kaa", 44),
    ("Mony",55),
];

students.sort(key = lambda student: student[1]);
print(students);


   # Sort a maps
numbers = [1,2,5,3,7];
square = list(map(lambda x: x*x, numbers));
print(square);
is_fliters = list(filter(lambda x: x % 2 ==0, numbers));
print(is_fliters);


    # Sorted a word
words = ["Banana","Cherry","Orange","Mango","Apple"];
sort_words = sorted(words, key = lambda word: len(words));
print(sort_words);