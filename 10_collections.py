   # Collections in python Programing
number = [1,2,3,4,5];
print(number);


   # Append
   
fruit = ["Apple","Banana","Cherry","Mango"];
fruit.append("Orange");
print(fruit);

   # Insert
items = ["Land","Home","Pagoda","Homeland"];
print(items);
items.insert(3, "Grape");
print(items);

    # Remove
items.remove("Home");
print(items);

   # Pop
items.pop();
print(items);

numbers = [10,20,30];
result = number.pop(1);
print(result);


    # Sort -> sorting the list of number by default
n = [1,2,3,4,5,6,7];
jj = n.sort(reverse=True);
print(jj);


    # reverse
items.reverse();
print(items);


    # Tuple
point = (10,20);
print(point);

    # Set
colors = {"Blue","Green"};
print(colors);
colors.add("Orange");
print(colors);
print(colors.remove);

    #Union
set1 = {1,2,3};
set2 = {3,4,5};
result = set1.union(set2);
print(result);



    # intersections
set1 = {1,2,3};
set2 = {3,4,5};
li = set1.intersection(set2);
print(li);


   # Dictionary
students = {
    "name": "John",
    "age": "20"
};

      #Key
print(students.keys());
      
      # Value
person = {
    "id" : 101,
    "name" : "Alice",
    "age" : 20,
};

   # value
print(person.values())

    #Items
print("Items : ", person.items())

    # get
persons = {
    "name" : "Alice",
    "age" : 20,
};

print(person.get("name"));
print(person.get("age"));

     # Update
print(person.update({"age" : 25}));
print(students);