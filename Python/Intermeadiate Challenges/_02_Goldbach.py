n = int(input())


def gold(num):
    x = []
    y = []
    z = []
    fac = 0
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                fac += 1
        if fac == 2:
            y.append(i)
        fac = 0
    for i in range(len(y)):
        for j in range(len(y)):
            if (y[i] + y[j]) == num:
                if j >= i:
                    z.append(y[i])
                    z.append(y[j])
                    x.append(z)
                    z = []
    return x


print(gold(n))
