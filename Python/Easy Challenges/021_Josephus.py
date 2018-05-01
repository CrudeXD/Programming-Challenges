

def exe(people,stPoint,skip):
    cur = 0 #current position
    y = []
    for i in range(people):
        y.append(i)
    while len(y) > 1:
        #for i in range(cur,len(y)):
            cur = ((cur + skip) % people)
            print(str(cur) +' '+str(people))
            #del y[cur]
            y.pop(cur)
    return y


print(exe(6,0,2))
