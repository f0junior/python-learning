while True:
    peso = float(input("Informe seu peso: "))
    altura = float(input("Informe sua altura: "))

    imc = peso / pow(altura, 2)

    print("Seu IMC deu {:.2f}, seu status é".format(imc), end="")
    if imc > 40:
        print(" Obesidade Mórbida.")
    elif imc >= 30:
        print(" Obesidade.")
    elif imc >= 25:
        print(" Sobrepeso.")
    elif imc >= 18.5:
        print(" Peso Ideal.")
    else:
        print(" Abaixo do Peso.")
