    # Remove a file
import os


    # Open a file
file = open("folder.txt", "w");
file.write("Welcome to Python Programing...!");

    # Read a  file
file = open("folder.txt", "r");
print(file.read());

file.close();

    # Read 1 lines
file = open("folder.txt", "r");
print(file.readline());

file.close();


    # Read all lines
file = open("folder.txt");
print(file.readlines());

file.close();


     # Write into a file 
file = open("folder.txt", "w");
file.write("I like coding and Programing...!");

file.close();


    # Appending a data
file = open("folder.txt", "a");
file.write("\nI'm trying learning coding every days...");

file.close();


    # tesing writing text into a file
file = open("newfile.txt", "w");
file.write("I'm learning Clever IT Mobile Apps");

file.close();


    # close file
file = open("newfile.txt", "r");
file.close();



   # With open -> Automatically close auto (read)
with open("newfile.txt", "r") as file:
    print(file.read());
    


    # Write a file -> with open
with open("newfile.txt", "w") as file:
    file.write("Python Executive...!");
    
    
    # with open -> appending a text file
with open("newfile.txt", "a") as file:
    file.write("\nPython Programing goods...!");
    
    # checking a file when file is see
if os.path.exists("newfile.txt"):
    print("file exists...!");
else:
    print("file not found...!");


if os.path.exists("folder.txt"):
    print("file exists...!");
else:
    print("file not found...!");
    
    
    
        # Remove a file
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt");
    print("REMOVE FILE SUCCESUFULLY...!");
else:
    print("file not found...!");
    
    
        # Copying a file
with open("folder.txt", "r") as source:
    content = source.read();
    
with open("newfile.txt", "w") as destination:
    destination.write(content);
    
print("file copy succesfully...!");