min = int(input("Digite a faixa inferior: "))
max = int(input("Digite a faixa superior: "))
temp_max = max
pares = []

for i in range(min, max + 1):
    if i % 2 == 0:
        pares.append(i)
for i in range(min, max + 1):
    print(temp_max, end = " ")
    temp_max -= 1
print("\nA quantidade de pares entre " + str(min) + " e " + str(max) + " é: " + str(len(pares)))