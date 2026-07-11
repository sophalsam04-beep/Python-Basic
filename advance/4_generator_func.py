def numbers():
    yield 1
    yield 2
    yield 3
    
    
for n in numbers():
    print(n)
    
    
    # Generator expression
square = (x ** 2 for x in range(5))

for i in square:
    print(i)