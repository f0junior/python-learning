while True:
    nome = input("Informe seu nome completo: ").strip()
    print("Seu nome em maiúsculo é {}.".format(nome.upper()))
    print("Seu nome em minúsculo é {}.".format(nome.lower()))
    print("Seu nome tem ao todo {} letras.".format(len(nome.replace(" ", ""))))
    print(
        "Seu primeiro nome é {} e tem ao todo {} letras.".format(
            nome.split()[0], len(nome.split()[0])
        )
    )
