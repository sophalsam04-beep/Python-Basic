#Nested looping in python
#Nested loop is a if into if statement

age = 20;
has_id = True;
if age>=18:
    if has_id:
        print("Entry allowed !");
    else:
        print("ID Required");
else:
    print("Underage");
    


temperature = 38;
has_sicks = True;
if temperature>37:
    if has_id:
        print("Entry allowed");
    else:
        print("ID Required");
else:
    print("Underage");