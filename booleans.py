v = True
f = False

print(5>3) #V
print(3>4) #F
print(type(v))

print(bool("Hola Mundo"))
print(bool(""))

# True
print(bool("abc"))
print(bool(123))
print(bool(["Manzana", "Pera"]))

#False
print(bool([]))
print(bool(0))
print(bool(""))
print(bool(None))

x = 123
print(isinstance(x, int))

x = 123.5
print(isinstance(x, int))