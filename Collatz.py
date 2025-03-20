print("-----------------Sequência de Collatz-----------------")
numero = int(input("Insira um numero na sequencia de Collatz: "))
inicial = numero
passos = 0
while True:
    if numero == 1:
        print(int(numero))
        break
    elif (numero % 2 == 0):
        print(int(numero), end=" → ")
        numero = numero/2
        passos += 1
    elif numero % 2 != 0:
        print(int(numero), end=" → ")
        numero = (numero*3)+1
        passos += 1
print()
print(f"Foram neccessarios {passos} passos para chegar até o numero 1 a partir do numero {int(inicial)}")
print("-----------------Sequência de Collatz-----------------")