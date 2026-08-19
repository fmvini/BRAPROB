import random

x = random.randint(1, 100)   
y = random.randint(101, 200) 

numero = int(input("Digite um número inteiro: "))

if x <= numero <= y:
    print(f"O número {numero} está dentro da faixa ({x} a {y}).")
else:
    print(f"O número {numero} NÃO está dentro da faixa ({x} a {y}).")