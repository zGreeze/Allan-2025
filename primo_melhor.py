import math
import random
def is_prime(num):
    if (num <= 1):
        return False
    iteracao = 2
    while (iteracao <= int(math.sqrt(num))):
        if num % iteracao == 0:
            return False
        else:
            iteracao +=1
    return True


def max_multiplo(num):
    if (num < 1):
        return False
    i = int(num/2)
    if is_prime(num):
        return 1
    while i >= 2:
        if (is_prime(i)) and (num % i == 0):
            return int(i)
        i -= 1

def maior_primo_ate (num):
    i = num
    while i > 2:
        if is_prime(i) == True:
            return i
        i -= 1
print(maior_primo_ate(1000000))

print(12)


