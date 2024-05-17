from random import randint

while True:
    jogador = int(input("Escolha ([1] Pedra, [2] Papel e [3] Tesoura): "))
    maquina = randint(1, 3)

    if jogador == maquina:
        print("Empate, escolhemos a mesma coisa.")
        continue

    match (jogador):
        case 1:
            if maquina == 2:
                print("Ganhei!! Você escolheu Pedra e eu escolhi Papel.")
            else:
                print("Você ganhou!! Você escolheu Pedra e eu escolhi Tesoura.")

        case 2:
            if maquina == 1:
                print("Você ganhou!! Você escolheu Papel e eu escolhi Pedra.")
            else:
                print("Ganhei!! Você escolheu Papel e eu escolhi Tesoura.")
        case 3:
            if maquina == 1:
                print("Ganhei!! Você escolheu Tesoura e eu escolhi Pedra")
            else:
                print("Você ganhou!! Você escolheu Tesoura e eu escolhi Papel")
        case _:
            print("Opção inválida.")
            continue
