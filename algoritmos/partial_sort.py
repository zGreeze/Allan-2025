def sort_array(lista):
    lista = lista
    # Criar uma lista com os impares ordenados
    impares = []
    for i in lista:
        if i % 2 != 0:
            impares.append(i)
    impares.sort()

    # Criar uma lista com o indice de cada numero impar
    indices = []
    a = 0
    for x in lista:
        if x % 2 != 0:
            indices.append(lista.index(x, a))
        a += 1
    # Algoritimo
    impind = 0
    for i in indices:
        lista[i] = impares[impind]
        impind += 1
    return lista

print(sort_array([1, 111, 11, 11, 2, 1, 5, 0]))











