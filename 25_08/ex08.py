from random import randint
lista = []

for i in range(18):
    lista.append(i + 1)

sorteado = []

for i in range(18):
    x = randint(0, (17 - i))
    sorteado.append(lista[x])
    lista.remove(lista[x])

for i in range(18):
    print("Nº", i + 1, "->", sorteado[i])