x = [3,6,9,1,2,5,0,11,6]
maxi = x[0]

for i in range(len(x)):
  if maxi < x[i]:
    maxi = x[i]

print(maxi)
