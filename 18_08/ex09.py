def bubble_sort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

x = int(input("Digite o tamanho da lista: "))
lista = [0] * x
for i in range(x):
    lista[i] = int(input("Digite um número: "))
print("Lista original:", lista)
bubble_sort(lista)
print("Lista ordenada:", lista)