fname = 'data.txt'


file = open(fname, 'w')

for i in range(10):
    file.write('This is line {} \n'.format(str(i)))
file.close()

file = open(fname, 'r')

for line in file:
    print(line, end = '')
file.close()
