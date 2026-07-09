   # Learning Methods
   
   # Upper case
text = "Hello Programing";
print("Convert Lower case to Uppercase : ", text.upper());
    # Lower case
print("Convert Uppercase to lower case : "+text.lower());

# Replace
txt = "I like Java";
print(txt.replace("Java", "Python"));
t = "I'm Clever of Coding...!";
print(t.replace("Coding", "Programing"));

# Multiple Occurent text
ji = "apple apple apple apple";
print(ji.replace("apple", "orange"));


   # Split -> convert string to list
table = "Java Developers...!";
print(table.split());
gui = "Javascript";
print(gui.split());

gg = "Backend, Framework, Programing, Developers";
print(gg.split(","));


array = "             Hello Python              ";
print(array.strip());


   # find -> Return the index of numbers
   
ff = "Hello C++";
print(ff.find("C++"));

tee = "Welcome to Java Programing...!";
print(tee.find("Programing...!"));


    #Startswitch -> check whether strinig start with specific prefix
    
trr = "Hello Javascript";
print(trr.startswith("Hello"));
print(trr.startswith("Javascript"));


   #endswitch -> check whether string end with specific suffix
   
hhh = "report.pdf";
print(hhh.endswith(".pdf"));
print(hhh.endswith(".doc"));