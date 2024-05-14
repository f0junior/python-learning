while True:
    v_casa = float(input("Informe o valor da casa: "))
    salario = float(input("Informe seu salário: "))
    anos = int(input("Informe em quantos anos vai pagar: "))

    prestacoes = v_casa / (anos * 12)
    minimo = salario * 0.3

    print("Para casa no valor de R$ {:.2f} em {} anos".format(v_casa, anos), end="")
    print(" a prestação será de R$ {:.2f}.".format(prestacoes))

    if prestacoes > minimo:
        print(
            "Empréstimo negado, pois o valor supera trinta por cento de seu salário R$ {:.2f}.".format(
                minimo
            )
        )
        continue

    print("Emprestimo aprovado.")
