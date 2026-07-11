from functools import reduce

  # Nested functions
def outer():
    print("Outer function...!");
    
def inner():
    print("Inner function...!");
    
inner();
outer();


    # Reursive functions
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1);

print(factorial(5));

def recursive(a):
    if a == 1:
        return 1
    return a * recursive(a-1);


print(recursive(4));
    
    
      # Functions return another functions
def multiply(x):
    def inner(y):
        return x*y;
    
    return inner
double = multiply(2);
print(double(5));
    
    
    # Maps
number = [1,2,3,4,5];
result = list(map(lambda x: x*2, number));
print(result);


    # Fliters
num = [1,2,3,4,5];
answer = list(filter(lambda y: y % 2 == 0, number));
print(answer);



   # Reduces
number = [1,2,3,4];
result = reduce(lambda x,y : x+y, number);

print(result)


  # Decorator
def decorator(func):
    def wrapper():
        print("Before functions...!");
        func();
        print("After functions...!");
    return wrapper
@decorator
def hello():
    print("Hello world");

hello()



   # Closure
def outer(message):
    def inner():
        print(message);
    return inner()

greet = outer("Hello world");
