x = [1,2,3,1,3,3,2,1,4,5,5,5,6]

def dupCrush(list):
    y = []
    for i in range(len(list)):
        if list[i] not in y:
            y.append(list[i])

    return y
print(dupCrush(x))
