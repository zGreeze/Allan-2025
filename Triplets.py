triplets = [
          ['t','u','p'],
          ['w','h','i'],
          ['t','s','u'],
          ['a','t','s'],
          ['h','a','p'],
          ['t','i','s'],
          ['w','h','s']
        ]

def recover_secret(triplets):

# Função

    string_final = []

    # Loop

    continuar = 7
    while continuar > 0:

        # Candidatos a primeira letra

        candprim = []
        for i in range (len(triplets)):
            if len(triplets[i]) > 0 :
                candprim.append(triplets[i][0])
        candprim = list(set(candprim))

        # Achar a primeira letra da string

        while len(candprim) > 1:
            for cand in candprim:
                for i in range(len(triplets)):
                    if cand in triplets[i]:
                        if triplets[i].index(cand) != 0:
                            candprim.remove(cand)
                            break
        string_final.append(candprim[0])

        # Remover a primeira letra dos triplets

        for i in range(len(triplets)):
            if candprim[0] in triplets[i]:
                triplets[i].remove(candprim[0])

        # Parametro para continuar

        a = 0
        for i in range(len(triplets)):
            if len(triplets[i]) > 0:
                a += 1
        continuar = a
    return "".join(string_final)
print(recover_secret(triplets))