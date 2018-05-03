from random import randint

print('Guess any whole number from 1 to 20')
minNum = 1
maxNum = 20
guess = randint(1, 20)
choice = ''
while choice != 'y':
    print('Is your num: {}. If not type y/n'.format(str(guess)))
    choice = input().lower()
    if choice == 'n':
        print('Higher [h] or lower [l]?')
        upDown = input().lower()
        if upDown == 'h':
            if guess >= minNum:
                minNum = guess
            guess = randint(minNum, maxNum)
        else:
            if guess <= maxNum:
                maxNum = guess
            guess = randint(minNum, maxNum)
    else:
        print('Hooray!')
        input()