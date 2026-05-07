frutas = ["Manzana", "Banana", "Mandarina", "Naranja"]

print(frutas[0]) # Manzana
print(frutas)

frutas[1] = "Pera"
print(frutas)

lista = [1, "Hola", True]
print(lista)

print(len(lista))
print(frutas[0:2])

if "Manzana" in frutas:
    print("La manzana está en la lista de frutas")
elif "Pera" in frutas:
    print("La pera está en la lista de frutas")

vehiculos = ["Auto", "Moto", "Avión"]
vehiculos.append("Barco")
vehiculos.insert(1, "Bicicleta")
vehiculos.remove("Auto")
vehiculos.pop(2) # Elimina el elemento en la posición 2 (Avión)
vehiculos.sort()
vehiculos.reverse()
print(vehiculos)

coleccion = [1, 2, 3]
coleccion2 = [4, 5, 6]
coleccion3 = coleccion + coleccion2
print(coleccion3)

coleccion.extend(coleccion2)
print(coleccion)

