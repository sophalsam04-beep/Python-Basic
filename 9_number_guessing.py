   # number guessing
while True:
    number = int(input("Enter number greater than 10 : "));
    
    if number > 10:
        print("Correct number...!");
        break;
    print("Try a again...!");
    
    
while True:
    print("=====MENU====");
    print("1. Start");
    print("2. Exist");
    
    choose = input("Choose : ");
    
    if choose == "1":
        print("The program is running...!");
    elif choose == "2":
        print("Good bye");
        break;
    else:
        print("Invalid correct");