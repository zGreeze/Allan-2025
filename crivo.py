import math

numero_principal = 100000
iteracao_inicio = round(math.sqrt(numero_principal))
primos_sqrt = list(range(1, iteracao_inicio + 1))

def crivo(iteracao, primos):
    ind = 0
    for x in range (2, round(math.sqrt(iteracao)) + 1):
        num = primos[ind]
        for i in primos:
            if i == primos[ind]:
                pass
            elif i % num == 0:
                primos.remove(i)
        ind +=1
    print(primos)
    print(len(primos))

crivo(iteracao_inicio, primos_sqrt)

iteracao_meio = len(primos_sqrt)
primos_meio = list(range(1,numero_principal+1))
ind = 0

for z in range (1, iteracao_meio+1):
    num = primos_meio[ind]
    for k in primos_meio:
        if k == primos_meio[ind]:
            pass
        elif k % num == 0:
            primos_meio.remove(k)
    ind+=1
print(primos_meio)
print(len(primos_meio))







