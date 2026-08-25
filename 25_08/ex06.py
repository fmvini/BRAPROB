idades = [34, 12, 98, 66, 45, 101, 3, 50]
soma = 0
pares = 0
for i in range(len(idades)):
    soma += idades[i]
print(soma)

media = soma / len(idades)
print(media)

for i in range(len(idades) + 1):
    if i % 2 == 0:
        pares += 1
print(pares)