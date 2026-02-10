#using to math to caculate
import math

x1 = float(input("Enter number x1 : "));
x2 = float(input("Enter number x2 :"));
x3 = float(input("Enter number x3 :"));
y1 = float(input("Enter number y1 "));
y2 = float(input("Enter number y2 :"));

distance = math.sqrt((x2 - x1)**2 + (y2 -y1) ** 2);
meter = math.sqrt((y2+y1)**2 - (x1-x2)**3);
kilo = math.sqrt((y1-y2) ** 5 + (x1 - x2));
t1 = math.log(10);
t2 = math.log1p;
t3 = math.log10;
t4 = math.lgamma(3.2);

print("The result of the distance : ", distance);
print("The result of the meter :", meter);
print("The result of the kilo : ", kilo);
print(t1);
print(t2);
print(t3);
print(t4);

print(math.floor(12));
print(math.ceil(4.3));
print(math.factorial(4.3*2)-1);

print(math.pi);
print(math.tau);
print(math.e);