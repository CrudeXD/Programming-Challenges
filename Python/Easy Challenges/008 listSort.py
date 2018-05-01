x = [2,9,4,6]
y = [7,8,3,5]
z = []
maxi = x[0]
pos = 0
print('x: '+str(x))
print('y: '+str(y))

for i in range(len(y)):
  x.append(y[i])

for j in range(len(x)-1):
    maxi = x[0]
    for i in range(len(x)):
        if maxi < x[i]:
            maxi = x[i]
            pos = i
    z.append(maxi)
    del x[pos]
z.append(x[0])
print('z: '+str(z))
