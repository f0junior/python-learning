while True:
    numero = int(input("Informe um número inteiro: "))
    tabuada = []
    for x in range(1, 11):
        tabuada.append(numero * x)

    print("Tabuada de {}".format(numero))
    print("-" * 12)
    multiplicador = 1
    for x in tabuada:
        print("{} x {:2} = {}".format(numero, multiplicador, x))
        multiplicador += 1

    print("-" * 12)
