i = 1

while i < 10:
    print(i)
    if i == 5:
        break
    if i == 6:
        continue
    i += 1
else:
    print("El ciclo ha terminado")