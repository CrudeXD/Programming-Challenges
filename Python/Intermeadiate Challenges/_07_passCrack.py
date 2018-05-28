import math
global guess
import time
import stopwatch


pasw = str(input('Input password: '))
chars = 'abcdefghijklmnopqrstuvwxyz'  # only limeted myself to lowercase for simpllicity.
base = len(chars)+1


def cracker(pasw):
    ti = time.time()
    guess = ''
    tests = 1
    c = 0
    m = 0

    while True:
        y = tests
        while True:
            c = y % base
            m = math.floor((y - c) / base)
            y = m
            guess = chars[(c - 1)] + guess
            if m == 0:
                break
        print(guess)
        if guess == pasw:
            tf = time.time()
            print('Got "{}" after {} tests {}'.format(
                guess, str(tests), stopwatch.stopwatch(ti, tf)))
            break
        else:
            tests += 1
            guess = ''


cracker(pasw)
input()
