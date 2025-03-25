import random

usuario = 0
computador = 0
dice = 0
round = 1
user_victory = 0
comp_victory = 0
print("---------------------------O primeiro a chegar a 30 pontos ganha-----------------------------------")
print("\nMelhor de 3")
while (user_victory < 2) and (comp_victory < 2) :
    while ((usuario < 30) and (computador < 30)) or (abs(usuario-computador) < 3 ):
        print(f"\n\n==================ROUND {round}=====================")
        user_confirm = str(input("\n\nAperte enter para jogar o dado (q para parar)\n"))
        if user_confirm.lower() != "q":
            dice = random.randint(1,6)
        else:
            break
        print(f"\nVoce ganhou {dice} pontos")
        usuario += dice
        dice = random.randint(1,6)
        print(f"O computador ganhou {dice} pontos")
        computador += dice
        print(f"\n\nUsuario : {usuario}")
        print(f"Computador: {computador}")

    if usuario > computador:
        print("\nVoce ganhou a rodada!")
        user_victory += 1
    elif computador > usuario:
        print("\nVoce perdeu a rodada")
        comp_victory +=1
    else:
        print("\nO jogo foi interrompido")
        break
    usuario = 0
    computador = 0
    round +=1
    print(f"Vitorias do usuario : {user_victory}")
    print(f"Vitorias do computador: {comp_victory}")

if user_victory == 2:
    print("\n\nParabens voce ganhou a partida!")
else:
    print("\n\nVoce perdeu a partida, mais sorte na proxima")