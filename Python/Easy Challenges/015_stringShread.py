
def stringShred(string):
    x = []
    y = []
    string.lower()
    for i in range(len(string)):
        x.append(string[i])
        x.sort()
    for i in range(len(x)):  # ['e', 'h', 'l', 'l', 'o']
        if x[i] not in y:
            y.append(x[i])
    return y


print(stringShred('hello'))
