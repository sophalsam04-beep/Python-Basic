   # Step1
numbers = iter([1,2,3,4,5]);
print(next(numbers));

    # Step2
number = [1,2,3,4,5];
it = iter(number);
print(next(it));
print(next(it));
print(next(it));
print(next(it));
print(next(it));


    # Step3
fruit = ["Apple","Banana","Mango"];

for f in fruit:
    print(f);
    
        
        # Step4 -> Dictionary
        
stuednt = {
       "name ": "Un virak",
       "age" : 20,
   }
   
itel = iter(stuednt);
print(next(itel));