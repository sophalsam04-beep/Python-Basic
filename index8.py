## 10-Feb-2026
## Learning Python Programming about Operator 

x = 100;
y = 63;
#arithmetic operator

result = (x+y);
result1 = (x-y);
result2 = (x*y);
result3 = (x/y);
result4 = (x//y);
result5 = (x%y);
result6 = (x-y+(x*2-3)+5);
result7 = (x+y-1);

#print the result
print(f"The result : {result}");
print(f"The result : {result1}");
print(f"The result : {result2}");
print(f"The result : {result3}");
print(f"The result : {result4}");
print(f"The result : {result5}");
print(f"The result : {result6}");
print(f"The result : {result7}");


## Assignment operator
a = 43;
a+=43;
print(a);
c = 30;
d = +a;
print(d);

b = 10;
b+=55;
print(b);

bg = 77;
bg+=43;
print(bg);

gd = 20;
gd/=76;
print(gd);

ll = 10;
ll%=30;
print(ll);

# Comparision operator is Boolean compare two value

number1 = 42;
number2 = 44;

print(number1 == number2);
print(number1 // number2);
print(number2 >= number1);
print(number2<=number1);
print(number1!=number2);
print(number1>number2);
print(number2<number1);

# Logical opertor
ages = 20;
print(ages>18 and ages< 30);
print(ages < 18 and ages == 20);
print(ages is 19);

#is operator --> using to compare memory locations
x1 = 39;
x2 = 33;
print(a is b);
print(b is a)