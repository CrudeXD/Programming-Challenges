state =[]
doors = 100

for i in range(doors):
    state.append(1)

for j in range(1,doors+1):
    for i in range(int(doors/j)):
        if state[i*j] == 1:
            state[i] = 0
        else:
            state[i] = 1

print(state)

# Not Done!
