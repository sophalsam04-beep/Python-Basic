#What is the Function?
#function is a block of code that specify code of task
# function definition
#function with return value
#function with parameter

def caculate():
    print("The result of function !");
    
caculate()


def greet(name):
    print("Hello !", name);
    
greet("Daroth");
greet("Phal");

#function with return value
def value(a, b):
    return (a+b);

result = value(3,6);
print(result);

#Using to Multiple Arugnment
def add_number(*nums):
    total = 0;
    for n in nums:
        total+=n;
    return total;

print(add_number(1,2,3,4,5));


def sub_number(*num):
    sub = 0;
    for s in num:
        sub -=s;
    return sub;

print(sub_number(5,4));