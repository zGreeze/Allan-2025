def opera(ops):

    # Variaveis

    altura = 0
    eixox = 0
    #Ajustar a altura

    for movimento in ops :
        altura -= movimento[1]

    #Ajustar a distancia no eixo do x

    for ajustex in ops:
        if ajustex[0] == "l":
            eixox -= 1
        elif ajustex[0] == "r":
            eixox += 1
    if eixox > 0:
        distancia = "l"
    elif eixox < 0:
        distancia = "r"
    else:
        distancia = "s"

    return (distancia,altura)
print(opera([('r', -6), ('l', 6), ('s', 5)]))