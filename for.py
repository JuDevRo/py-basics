palabra = "Python"

for letra in palabra:
    print(letra)

frutas = ["manzana", "banana", "naranja"]
adjetivos = ["roja", "amarilla", "naranja"]

for fruta in frutas:
    print(fruta)

for fruta in frutas:
    if fruta == "banana":
        break
    print(fruta)

for fruta in frutas:
    if fruta == "banana":
        continue
    print(fruta)
else:
    print("El ciclo ha terminado")

for i in range(10):
    print(i) # No incluye el 10

for i in range(5, 10):
    print(i) # No incluye el 10, empieza en el 5

for i in range(5, 10, 2):
    print(i) # No incluye el 10, empieza en el 5, saltando de a 2

for adejtivo in adjetivos:
    for fruta in frutas:
        print(f"{fruta} {adejtivo}")
