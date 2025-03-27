# Exercicio 5.1

def fatorial(n:int):
    if n < 0:
        return "invalido"
    if n == 0:
        return 1
    listfac = list(range(1,n))
    for i in listfac:
        n *= i
    return n
def binom (n,k):
    try:
        return int((fatorial(n))/((fatorial(k))*fatorial(n-k)))
    except ValueError:
        return "invalido"

# Exercicio 5.2

def apenas_letras_nospace(txt:str):  # Não pode espaço
    return txt.isalpha()

def apenas_letras(txt:str):     # Pode espaço
    txt = txt.replace(" ","")
    return txt.isalpha()

# Exercicio 5.3

def filtra_letras(txt: str):
    for i in txt:
        if not i.isalpha():
            txt = txt.replace(i, "")
    return txt

# Exercicio 5.4

def inversa(txt: str):
    lista = list(reversed(txt))
    return "".join(lista)

# Exercicio 5.5 e 5.6

def palindromo(txt: str):
    transformar = [i.lower() for i in txt if i.isalpha() == True]
    if list(reversed(transformar)) == transformar:
        return True
    else:
        return False

# Exercicio 5.7

def rem_espacos(txt: str):
    lista = txt.split()
    while " " in lista:
        lista.remove(" ")
    return " ".join(lista)

#  Exercicio 5.8

def vinegere(chave: str, palavra: str):
    if (chave.isalpha() == False) or (palavra.isalpha() == False):
        return "A palavra pode apenas conter letras basicas do alfabeto para ser cifrada"
    desl = [ord (letra) - 97 for letra in chave.lower()]
    cifr = [ord (i) - 97 for i in palavra.lower()]
    mod = len(chave)
    indic  = 0
    while indic < len(cifr):
        point = indic % mod
        cifr[indic] = (cifr[indic] + desl[point]) % 26
        indic += 1
    final = [chr (alg+97) for alg in cifr]
    return "".join(final).upper()

# Exercicio extra

def descrip_vinegere(chave: str, palavra: str):
    if (chave.isalpha() == False) or (palavra.isalpha() == False):
        return "A palavra pode apenas conter letras basicas do alfabeto para ser cifrada"
    desl = [ord (letra) - 97 for letra in chave.lower()]
    cifr = [ord (i) - 97 for i in palavra.lower()]
    mod = len(chave)
    indic  = 0
    while indic < len(cifr):
        point = indic % mod
        cifr[indic] = (cifr[indic] - desl[point]) % 26
        indic += 1
    final = [chr (alg+97) for alg in cifr]
    return "".join(final).upper()

# Parentesis

def parentesis(texto:str)->bool:
    for i in texto:
        if (i != "(") and (i != ")"):
            texto = texto.replace(i,"")
    lista = list(texto)
    if (lista.count("(") == 0) and (lista.count(")") ==0):
        return True
   # if lista.count("(") != lista.count(")"):
       # return False
    while len(lista) > 0:
        try:
            if lista.index("(") < lista.index(")"):
                lista.remove("("), lista.remove(")")
            else:
                print(lista)
                return False
        except ValueError:
            return False
    return True
