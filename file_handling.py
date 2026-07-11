import os

  # Read a file
file = open("example.txt");
content = file.read();

print(content);
file.close();


  # Read one lines
print(file.readline())
file.close();

  # Read all lines
lines = file.readlines();
print(file);
file.close();


  # Write a file
file = open("example.txt", "w");
file.write("Hello! Python Programing...!")



    #Appending a file
file = open("example.txt", "a");
file.write("Learning Mobile Apps developments");
file.close();

    # Create a new file
file = open("example.txt", "x");
file.close();


   # statements With ( Read ) closing file after used

with open("example.txt", "r") as file:
    print(file.read());
    
   # Statements With (Write) closing file after used
with open("example.txt", "w") as file:
    file.write("Python File handling...!");
    
os.remove("example.txt");



      # counting word in a file
with open("newfile.txt", "r") as file:
  text = file.read();
  
words = text.split()

print("Number of words ; ", len(words));


      # try catch
try:
  with open("newfile.txt", "r") as file:
    print(file.read());
  
except FileNotFoundError:
  print("file not found...!");