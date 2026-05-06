x = 5
y = 7
z = 1

if x > y:
    print("x es mayor que y")
else:
    print("x no es mayor que y")

if x > y:
    print("x es mayor que y")
elif x == y:
    print("x es igual a y")
else:
    print("x no es mayor que y")

if x > y and x > z:
    print("x es el mayor")
elif y > x and y > z:
    print("y es el mayor")
else:
    print("z es el mayor")
    
if x > y or x > z:
    print("x es el mayor")
elif y > x or y > z:
    print("y es el mayor")
else:
    print("z es el mayor")

if y > x:
    if y > z:
        print("y es el mayor")

if x == y: 
    pass #Ignora el if hasta definir el comportamiento