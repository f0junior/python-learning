while True:
    numero = int(input("Informe um número inteiro: "))
    tabuada = []
    for x in range(1, 11):
        tabuada.append(numero * x)

    print("Tabuada de {}".format(numero))
    multiplicador = 1
    for x in tabuada:
        print("{}x{}= {}".format(numero, multiplicador, x))
        multiplicador += 1
