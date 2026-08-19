import random

min = int(input("Digite a faixa inferior: "))
max = int(input("Digite a faixa superior: "))
contador = 0
x = random.randint(min, max)   

numero = int(input("Digite um número inteiro: "))
while numero != x:
    if x < numero:
        print(f"O número aleatorio é menor que {numero}.")
    else:
        print(f"O número aleatorio é maior que {numero}.")
    contador += 1
    numero = int(input("Digite um número inteiro: "))

print(f"Voce acertou! O número aleatório é: {x}.")
print(f"Voce errou {contador} vezes!")