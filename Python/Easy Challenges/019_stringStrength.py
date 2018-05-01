x = "this is cool"

def sStr(string):
    dmg = 0 #the 'damage' value of the strength of the word
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    y = string.split()
    for i in range(len(y)):
        for j in range(len(y[i])):
            for k in range(len(alpha)):
                if y[i][j] == alpha[k]:
                    dmg += (k + 1)
    return dmg


print(sStr(x))
