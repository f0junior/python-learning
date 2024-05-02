while True:
    nome = input("Informe seu nome: ").strip()
    nomePartido = nome.split()
    print("Seu primeiro nome é {}.".format(nomePartido[0]))
    print("Seu último nome é {}.".format(nomePartido[len(nomePartido) - 1]))
