while True:
    print("Vamos calcular a média aritmética.")

    maisNumero = "s"
    numeros = []
    while maisNumero == "s" or maisNumero == "S":
        numeros.append(float(input("Informe um númmero: ")))

        maisNumero = input(
            "Deseja informar mais um número (s ou S para Sim, qualquer outro valor para não): "
        )

    print("A média aritmética dos números: ", end="")
    print(*numeros, sep=", ", end="")
    print(" é {}.".format(sum(numeros) / len(numeros)))
