while True:
    numero = input("Informe um número entre 0 e 9999: ")
    if len(numero) > 4:
        print("Número maior que o permitido.")
        continue

    print("Analisando o número {}.".format(numero))
    # for index, value in enumerate(numero):
    #     match (index):
    #         case 0:
    #             print("Unidade: {}".format(value))
    #         case 1:
    #             print("Dezena: {}".format(value))
    #         case 2:
    #             print("Centena: {}".format(value))
    #         case 3:
    #             print("Milhar: {}".format(value))

    numero = int(numero)
    print("Unidade: {}".format(numero % 10))
    print("Dezena: {}".format(numero // 10 % 10))
    print("Centena: {}".format(numero // 100 % 10))
    print("Milhar: {}".format(numero // 1000 % 10))
