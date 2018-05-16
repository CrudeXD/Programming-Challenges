fname = 'data.txt'
sum = 0
lines = []


file = open(fname, 'r')

for line in file:
    # print(str(line))
    lines.append(line)
file.close()

print(lines)
input()
