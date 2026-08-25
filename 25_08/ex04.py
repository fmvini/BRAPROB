pares = []
x = int(input("Inferior: "))
y = int(input("Superior: "))
for i in range(x, y, 1):
    if i % 2 == 0:
        pares.append(i)
print(pares)