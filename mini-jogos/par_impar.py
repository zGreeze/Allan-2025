import random

def par_impar(usuario:int, computador:int):
    if (usuario + computador) % 2 == 0:
        return "par"
    else:
        return "impar"
print("----------Bem vindo ao jogo de par ou impar contra o computador----------")
maximo = int(input("Qual o maximo de rodadas da sua serie?\n----> "))

rodadas = 1
vitorias_computador = 0
vitorias_usuario = 0
while True:
    print(f"-----------------Rodada {rodadas}-------------------")
    choice = str(input("par ou impar? (q para interromper) \n ----> "))
    while True:
        if choice.lower() == "q":
            break
        if choice.lower() == "impar":
            break
        elif choice.lower() == "par":
            break
        else:
            choice = str(input("par ou impar? \n ----> "))
    if choice.lower() == "q":
        break
    computer = random.randint(1,10)
    user = int(input("insira um numero entre 0 a 10: "))
    while (user < 0) or (user> 10):
        user = int(input("insira um numero entre 0 a 10: "))

    print(f"\nComputador jogou: {computer} \nUsuario jogou: {user}")

    if par_impar(user, computer) != choice.lower():
        print("\nVoce perdeu")
        vitorias_computador += 1
    else:
        print("\nVoce ganhou")
        vitorias_usuario += 1
    print(f"\nUsuario: {vitorias_usuario} \nComputador: {vitorias_computador}\n\n")
    if vitorias_computador > maximo/2:
        print(f"O computador ganhou a serie em {rodadas} rodadas")
        break
    elif vitorias_usuario > maximo/2:
        print(f"Parabens! voce ganhou a serie em {rodadas} rodadas")
        break
    rodadas +=1