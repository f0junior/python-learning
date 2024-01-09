while True:
    valor = input("Informe um valor qualque: ")

    print(valor)
    print("isspace: {}".format(valor.isspace()))
    print("isalpha: {}".format(valor.isalpha()))
    print("isalnum: {}".format(valor.isalnum()))
    print("isascii: {}".format(valor.isascii()))
    print("islower: {}".format(valor.islower()))
    print("isupper: {}".format(valor.isupper()))
    print("istitle: {}".format(valor.istitle()))

    if valor.replace(".", "").isnumeric():
        valor = int(valor) if valor.find(".") == -1 else float(valor)

    print(type(valor))
    print(
        "Em python se convertido o valor {} em booleano, ele é: {}".format(
            valor, bool(valor)
        )
    )
