    # Module Import specific functions
    
import sys
import os
import datetime    
import random
from math import *
from pathlib import Path
import requests
from math import sqrt, factorial
import math;
import statistics
import random;

print(math.sqrt(25));
print(math.pi);
print(math.factorial(5));


print(random.randint(1,10));
print(random.choice(["Sophal","Bopha","morokot"]));


print(sqrt(5));
print(factorial(3));

print(math.pi);
print(math.acosh(4));
numbers = [10,20,30,40,50];
print(statistics.mean(numbers));



    # Requests
respone = requests.get("https://api.github.com");

print(respone.status_code);


print(random.randint(1,10));
print(random.random());
print(random.choices(["Apple","Banana","Cherry"]));
print(random.shuffle(numbers));


     # DateTime module
now = datetime.datetime.now();
print(now);
print(now.year);
print(now.month);
print(now.day);

    # Create a Date
birthdays = datetime.date(2005, 10,9);
print(birthdays);


print(os.getcwd());
print(sys.version);
print(sys.argv);



path = Path("example.txt");
print(path.exists);
print(path.suffix);
print(path.name);

   # Create a Directory file
Path("NewFolder").mkdir(exist_ok=True);


  # List of Python File
for file in Path(".").glob("*.py"):
    print(file);