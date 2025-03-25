def sum_two_smallest_numbers(numbers):
    lista_prov = numbers
    lista = []
    for i in lista_prov:
        if (i % 1 == 0) and (i > 0):
            lista.append(i)
    lista.sort()
    x = lista[0] + lista[1]
    return x
print(sum_two_smallest_numbers([-1,4564,43,123,43,654,234.2412,-241.543,2421.421,2,3]))




