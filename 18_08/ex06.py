min = int(input("Digite a faixa inferior: "))
max = int(input("Digite a faixa superior: "))
temp_max = max
pares = 0

for i in range(min, max + 1):
    if i % 2 == 0:
        pares += 1
for i in range(min, max + 1):
    print(temp_max)
    temp_max -= 1
print("A quantidade de pares entre " + str(min) + " e " + str(max) + " é: " + str(pares))