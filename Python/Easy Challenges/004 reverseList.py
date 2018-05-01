x = [3,6,9,1,2,5,0,11,6]
y = []
lenL = (len(x)-1)
for i in range(len(x)):
  y.append(x[(lenL - i)])

print(y)
