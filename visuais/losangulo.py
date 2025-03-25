linhas = int(input("Quantas linhas a parte superior do seu losangulo terá? \n \nLinhas: "))
num = 0
espaces = linhas
for i in range(1,linhas+1):
    print(" "*espaces,"*"*(i+num))
    espaces -= 1
    num += 1
espaces = 2
num = linhas + num - 3
for j in range(0,linhas-1):
    print(" "*espaces,"*"*(j+num))
    espaces += 1
    num -= 3