#Las tuplas son inmutables, es decir, no se pueden modificar después de su creación. Se definen utilizando paréntesis ().

tecnologias = ("Python", "Javascript", "Go")

print(tecnologias[0]) # Python
print(tecnologias)

print(len(tecnologias))

print(type(tecnologias)) # <class 'tuple'>

fruta = ("Manzana")

print(type(fruta)) # <class 'str'>

fruta = ("Manzana",)

print(type(fruta)) # <class 'tuple'>

tupla = (1, "Hola", True)
print(tupla)

x, y, z = tupla
print(x) # 1
print(y) # Hola
print(z) # True

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3) # (1, 2, 3, 4, 5, 6)

for item in tupla:
    print(item)

tuplaModificar = ("Python", "Javascript", "Go")
listaComodin = list(tuplaModificar)
print(listaComodin)
listaComodin.append("Java")
tuplaModificar = tuple(listaComodin)
print(tuplaModificar) # ('Python', 'Javascript', 'Go', 'Java')

# Las tuplas son tu elección cuando la integridad de los datos y la garantía de inmutabilidad son más importantes que la flexibilidad de modificación.

