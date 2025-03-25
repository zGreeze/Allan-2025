import math
numero = int(input("Reproduzir uma lista de todos os numeros primos de 1 ate : "))
numeros = list(range(1,numero+1))
primos = [2]
multiplos = []
for x in range (1, numero +2):
    for i in range (1,round(math.sqrt(x))):
        if not numero % numeros[i] == 0:
            multiplos.append(i)
        if multiplos.__len__() == round(math.sqrt(x)) - 1:
            primos.append(numero)
    multiplos.clear()
    numero = x
print(primos)