
def stringShred(string):
    x = []
    y = []
    count = 0
    pos = 0
    string.lower()
    for i in range(len(string)):
        x.append(string[i])
        x.sort()
    for i in range(len(x)):  #['e', 'h', 'l', 'l', 'o']
        for j in range(len(x)):
            if x[j] == x[i]:
                pos = j
                count += 1
        if count > 1:
            x.pop(pos)
        y.append(count)
        count = 0
    return y

print(stringShred('hello'))
