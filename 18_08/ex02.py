lista = [18, "Vinícius", 1.75, True]    

print(lista[0]) 
print(lista[1][0])
print(lista[2:4])

if lista[3]:
    print("Positivo.")
else: 
    print("Negativo.")

lista.append("Novo elemento")
print(lista)

lista.remove(lista[0])
print(lista)

lista.insert(0, 18)
print(lista)

lista_copia = lista.copy()
print(lista_copia)

