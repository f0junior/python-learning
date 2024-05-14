while True:
    numero = int(input("Informe um número inteiro: "))
    opcao = int(
        input(
            "Qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal: "
        )
    )

    match (opcao):
        case 1:
            print("{} em binário é {}.".format(numero, bin(numero)))
        case 2:
            print("{} em octal é {}.".format(numero, oct(numero)))
        case 3:
            print("{} em hexadecimal é {}.".format(numero, hex(numero)))
        case _:
            print("Opção inválida")
