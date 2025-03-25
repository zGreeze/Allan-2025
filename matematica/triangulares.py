import math
def triangulares_formula (n):
    return int((n*(n+1))/2)

def triangulares_inversa(n):
    return int((-1 + math.sqrt(1 + 8 * n)) / 2)

def triangulares_tuple(n):
    return tuple(triangulares_formula(i) for i in range (1, triangulares_inversa(n) + 1))

def triangular(n):
    numeros = triangulares_tuple(n)
    if n in numeros:
        return True
    else:
        return False

print(triangular(5050))
