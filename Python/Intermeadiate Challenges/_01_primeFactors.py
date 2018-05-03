n = int(input())

def primeFacs(num):
    x = [] #array to store all factors (prime and non-prime)
    y = [] #array to store all prime nums that can divide into n(prime factors).
    fac = 0 #number of factors a number has.
    for i in range(1,num+1):
        if num % (i) == 0: #To see if num is divisable by i. (Add 1 not to divide by 0)
            x.append(i)
            for j in range(1,i+1):
                if i % j == 0:
                    fac += 1
            if fac == 2: #If i, 'the factor of num' has two facors, it is prime. (To see if the factor only has two factors)
                y.append(i) #Append the original factor after it returns to be true(see if factor is prime).
            fac = 0
    return y


print(primeFacs(770))
input()
