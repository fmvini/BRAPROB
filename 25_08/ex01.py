lista = ["Ana", "Paula", "Julia", "Helena"]
for item in lista:
    if len(item) <= 4:
        lista.insert(1, "Vinícius")
    print(item, len(item))
print(lista)