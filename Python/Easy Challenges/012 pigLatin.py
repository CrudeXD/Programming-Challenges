#20
user = input('Insert a string: ')
x = user.split()
y = []
tmp = ''
trans = []

def strSplit(array, string):
  for i in range(len(string)):
    array.append(string[i])
  return array

for i in range(len(x)):
    trans = (strSplit(trans,x[i]))
    trans.append(trans[0])
    del trans[0]
    trans.append('a')
    trans.append('y')
    for i in range(len(trans)):
        tmp = tmp + trans[i]
    y.append(tmp)
    trans = []
    tmp = ''

for i in range(len(y)):
    tmp = tmp + y[i] + ' '

print(tmp)
input()
