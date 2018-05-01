x = [0,1]
fibo = 0
sum = 0

for i in range(100):
    fibo = x[-1] + x[-2]
    x.append(fibo)
    sum += fibo

print(x)
print(sum)
