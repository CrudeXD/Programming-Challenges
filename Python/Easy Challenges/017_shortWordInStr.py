x = 'Henlo this is a robery'


def shortStr(word):
    y = x.split()
    small = y[0]
    for i in range(len(y)):
        if len(small) < len(y[i]):
            small = y[i]
    return small

print(shortStr(x))
