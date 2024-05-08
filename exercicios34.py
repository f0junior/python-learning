while True:
    salario = float(input("Informe seu salário: "))
    aumento = 1.15
    if salario > 1250:
        aumento = 1.1

    print(
        "Seu salário vai de R$ {:.2f} para R$ {:.2f}.".format(
            salario, salario * aumento
        )
    )
