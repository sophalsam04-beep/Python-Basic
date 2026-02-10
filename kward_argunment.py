#using to kward argunment
def info(**detail):
    for key, value in detail.items():
        print(key,":", value);
        
info(name = "Daroth", age = 19, city = "Cambodia")