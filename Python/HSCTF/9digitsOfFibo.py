global flag


def getFlag():
    flag = ''
    fib = [0, 1]
    fibo = 0
    for i in range(48):
        fibo = fib[-1] + fib[-2]
        fib.append(fibo)
    for entry in fib:
        flag += str(entry)
    return flag[:-10:-1]


print(getFlag())
