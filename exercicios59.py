fim = False
numb_um = float(input("Informe o primeiro número: "))
numb_dois = float(input("Informe o segundo número: "))

while not fim:
    print("\nEscolha uma das opções abaixo: ")
    print(
        "[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa"
    )

    opcao = int(input("Opção escolhida: "))
    match (opcao):
        case 1:
            print(
                "{:.2f} + {:.2f} = {:.2f}".format(
                    numb_um, numb_dois, numb_um + numb_dois
                )
            )
        case 2:
            print(
                "{:.2f} x {:.2f} = {:.2f}".format(
                    numb_um, numb_dois, numb_um * numb_dois
                )
            )
        case 3:
            if numb_um > numb_dois:
                print("{:.2f} é maior que {:.2f}".format(numb_um, numb_dois))
            elif numb_dois > numb_um:
                print("{:.2f} é maior que {:.2f}".format(numb_dois, numb_um))
            else:
                print("Ambos os números tem o mesmo valor.")
        case 4:
            numb_um = float(input("Informe o primeiro número: "))
            numb_dois = float(input("Informe o segundo número: "))
        case 5:
            fim = True
            print("Programa finalizado.\n")
        case _:
            continue
