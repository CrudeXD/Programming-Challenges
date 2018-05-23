

def exe(people, stPoint, skip):
    cur = 0  # current position
    y = []
    for i in range(people):
        y.append(i)
    while len(y) > 0:
        print('cur: {}, People left: {}'.format(cur, y))
        cur = ((cur + skip) % len(y))
        y.pop(cur)
    return y


print(exe(6, 0, 2))
