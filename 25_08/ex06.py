idades = [34, 12, 98, 66, 45, 101, 3, 50]
pares = 0

soma = sum(idades)
print("Soma: ", soma)

media = soma / len(idades)
print("Media: ", media)

for i in range(len(idades)):
    if idades[i] % 2 == 0:
        pares += 1
print("Pares: ", pares)