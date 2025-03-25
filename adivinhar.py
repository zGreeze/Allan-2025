import random
low = 1
high = 100
awnser = random.randint(1, high)
max_guesses = 8
user = int(input(f"Insira um numero entre {low} e {high}, voce tem {max_guesses - 1} tentativas para acertar: "))
guesses = 1
while True:
    if user == awnser:
        print(f"voce acertou em {guesses} tentativas , o numero era {awnser} parabens!")
        break
    if guesses +1 == max_guesses:
        print(f"Voce perdeu por exceder o maximo de tentativas, o numero era {awnser} ")
        break
    if (user > high) or user < low :
       user = int(input("Insira um numero valido: "))
    elif user < awnser:
        print("Muito baixo, tente um numero maior")
        low = user
        guesses +=1
        print(f"Tentativas restantes: {max_guesses - guesses}")
        user = int(input(f"Insira um numero entre {low} e {high}: "))
    elif user > awnser:
        print("Muito alto, tente um numero menor")
        high = user
        guesses +=1
        print(f"Tentativas restantes: {max_guesses - guesses}")
        user = int(input(f"Insira um numero entre {low} e {high}: "))