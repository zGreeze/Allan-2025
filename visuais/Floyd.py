linha = int(input("Ate qual coluna do triangulo de Floyd voce quer ver? \nNumero: "))
list = [1]
print(*list)
len = 1
first = 1
list.pop(0)
for j in range(1,linha):
    for i in range(len+first,len+first+len+1):
        list.append(i)
        len = list.__len__()
        first = list[0]
    print(*list)
    list.clear()