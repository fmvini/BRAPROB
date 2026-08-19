fibo = [0, 1]
i = 1
while fibo[-1] < 1000:
    fibo.append(fibo[i] + fibo[i - 1])
    i += 1
fibo.remove(fibo[-1])
print(fibo)
