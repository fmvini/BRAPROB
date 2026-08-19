min = int(input("Digite a faixa inferior: "))
max = int(input("Digite a faixa superior: "))
pares = 0

for i in range(min, max + 1):
    if i % 2 == 0:
        pares += 1
    print(i, end=", ")
print("\nA quantidade de pares entre " + str(min) + " e " + str(max) + " é: " + str(pares))