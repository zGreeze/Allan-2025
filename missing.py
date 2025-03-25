# Letras minusculas
def minusculas (array):
    letras_minusculas = [chr(i) for i in range(97, 123)]
    inicio = letras_minusculas.index(array[0])
    x = 0
    for i in range (inicio, len(letras_minusculas)+1):
        if array[x] != letras_minusculas[i]:
            return letras_minusculas[i]
            break
        x += 1

# Letras maiusculas
def maiusculas (array):
    letras_maiusculas = [chr(i) for i in range(65,91)]
    inicio = letras_maiusculas.index(array[0])
    x = 0
    for i in range (inicio, len(letras_maiusculas)+1):
        if array[x] != letras_maiusculas[i]:
            return letras_maiusculas[i]
            break
        x += 1

# Função

def find_missing_letter(chars):
    if chars[0].isupper() == True:
        return maiusculas(chars)
    else:
        return minusculas(chars)