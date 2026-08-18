nome = input("Digite o nome do nadador: ")
idade = int(input("Digite a idade do nadador: "))
categoria = "nenhuma"

if 5 < idade <= 8:
    categoria = "Infantil A"
elif 8 < idade <= 10:
    categoria = "Infantil B"
elif 10 < idade <= 13:
    categoria = "Juvenil A"
elif 13 < idade <= 17:
    categoria = "Juvenil B"
elif 17 < idade:
    categoria = "Senior"

print("Nome: " + nome)
print("Categoria: " + categoria)