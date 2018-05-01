x = [1,2,3,4,5]
tmp = 0
k = 2 # k = rotation value

for i in range(k):
    x.append(x[0])
    del x[0]
    print(x)
