x = 'zabcd'

def nextLet(string):
    string.lower()
    y = string.split()
    z = []
    tmp = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(y)):
        for j in range(len(y[i])):
            for k in range(len(alpha)):
                if y[i][j] == alpha[k]:
                    if y[i][j] != 'z':
                        tmp = tmp + alpha[k+1]
                    else:
                        tmp = tmp + 'a'
        z.append(tmp)
        tmp = ''
    return z

print(nextLet(x))
