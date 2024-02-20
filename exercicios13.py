while True:
    salario = float(input("Informe seu salário: "))

    print(
        "Sendo seu salário R$ {:.2f} com 15% de aumento o novo valor será R$ {:.2f}".format(
            salario, salario * 1.15
        )
    )
