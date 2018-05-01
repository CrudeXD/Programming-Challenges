user = input('Insert a string: ')
x = user.split()
length = len(x[0])
space = 0

for i in range(len(x)):
    if length < len(x[i]):
        length = len(x[i])
    else:
        pass
print('*'*length + '**')

for i in range(len(x)):
    space = length - len(x[i])
    print('*' + x[i] + ' '*space + '*')

print('*'*length + '**')
