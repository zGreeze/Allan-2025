import random

options = ("pedra","papel","tesoura")
running = True
empates = 0
vitorias = 0
derrotas = 0

while running:

    player = None
    computer = random.choice(options)

    while (player not in options) and (player != "q"):
        player = input("Faça uma escolha valida (pedra, papel, tesoura): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print ("empate")
        empates += 1
    elif player == "papel" and computer == "pedra":
        print ("Vitoria")
        vitorias +=1
    elif player == "tesoura" and computer == "papel":
        print("Vitoria")
        vitorias += 1
    elif player == "pedra" and computer == "tesoura":
        print("Vitoria")
        vitorias += 1
    elif player == "q":
        running = False
    else:
        print("Derrota")
        derrotas += 1
    print(f"Vitorias: {vitorias}")
    print(f"Derrotas: {derrotas}")
    print(f"Empates: {empates}")
