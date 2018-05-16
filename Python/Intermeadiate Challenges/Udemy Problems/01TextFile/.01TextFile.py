fileName = 'data.txt'
data = ['Hello', 'I', 'like', 'python']

with open(fileName, mode='w') as f:
    for element in data:
        f.write(element)
        f.write('\n')
